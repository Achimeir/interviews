from typing import ByteString, Tuple

import flask
from lets_run import auth
from flask import (Blueprint, request, jsonify)
from flask import json
import base64
from lets_run.auth import create_keys
from lets_run.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')


def user_rank(user, rank_type, db) -> str:
    # get the user rank from the DB
    query_data = "" if rank_type == "overall" else f"WHERE {rank_type} = ?"
    try:
        user_id = str(user["id"])
        query = f"WITH Ranks AS(SELECT id, ROW_NUMBER() OVER( ORDER BY distance DESC) AS ranking FROM user {query_data}) SELECT ranking FROM Ranks WHERE id = {user_id}"

        if rank_type == "overall":
            return jsonify(dict(db.execute(query).fetchone()))
        elif rank_type == "city":
            return jsonify(dict(db.execute(query, [user["city"]]).fetchone()))
        elif rank_type == "age":
            return jsonify(dict(db.execute(query, [user["age"]]).fetchone()))
    except Exception as err:
        print(err)
    return jsonify({"ranking": -1})


def extract_request_data(new_json) -> Tuple[str, str, ByteString]:
    # extract the inner base64 JSON and the signature
    json_data, signature, encoded_json = None, None, None
    try:
        encoded_json, encoded_sig = new_json["request"].split(".")
        json_data = base64.b64decode(encoded_json.encode('utf-8'))
        json_data = json.loads(json_data)
        signature = base64.b64decode(encoded_sig.encode('utf-8'))

    except Exception as err:
        print(err)
    return signature, json_data, encoded_json


@bp.route('/signup', methods=(['POST', 'GET']))
def signup():

    public_key, private_key = None, None
    name, age, city = None, None, None
    if request.method == 'POST':
        db = get_db()
        user_data = request.get_json()

        # get the user data from the json
        try:
            name = user_data["name"]
            age = user_data["age"]
            city = user_data["city"]
        except:
            return jsonify({"error": "parameters in the request are missing"})

        #create public/private keys
        private_key, public_key = create_keys()

        #add the user to the DB with it's public key and 0 distance
        db.execute(
            'INSERT INTO user (name, age, city, distance, public_key) VALUES (?,?,?,?,?)', (
                name, age, city, 0, public_key.exportKey())
        )
        db.commit()

        #return the private key
        return jsonify({"private_key": private_key.exportKey().decode('utf-8') if private_key else None})


@bp.route('/update', methods=(['POST', 'GET']))
def update():
    if request.method == 'POST':
        request_data = request.get_json()
        db = get_db()
        try:
            public_key = None
            #extract the data from the base64 json
            signature, json_data, json_data_encoded = extract_request_data(
                request_data)
            #get the user name
            name = json_data["name"]

            #iterate over all the users with the given name and check if their public key can verify the signature
            # because of maybe their are multiple users with the same name so name is not good enough
            for user in db.execute('SELECT * FROM user WHERE name = ?', [name]).fetchall():
                public_key = user["public_key"].decode('utf-8')

                if auth.verify_signature(public_key, json_data_encoded, signature):
                    #if the signaure on the request is verified we update the distance of the user
                    db.execute('UPDATE user SET distance = ? WHERE public_key=?', [
                               user["distance"]+json_data["distance"], user["public_key"]])
                    db.commit()

                    #get the updated distance from the DB
                    output = dict(db.execute(
                        'SELECT * FROM user WHERE public_key = ?', [user["public_key"]]).fetchone())
                    return jsonify({"totalDistanceRun": output["distance"]})
            print("didn't find the signer")
        except Exception as err:
            print(err)
        return jsonify({"totalDistanceRun": -1})


@bp.route('/mystats', methods=(['POST', 'GET']))
def stats():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            db = get_db()
            public_key = None
            #extract the data from the base64 json
            signature, json_data, json_data_encoded = extract_request_data(
                request_data)
            name = json_data["name"]

            #iterate over all the users with the given name
            for user in db.execute('SELECT * FROM user WHERE name = ?', [name]).fetchall():
                public_key = user["public_key"].decode('utf-8')

                #verify the signature
                if auth.verify_signature(public_key, json_data_encoded, signature):
                    #check the rank of the user in the given group (city, age, overall)
                    return user_rank(user, json_data["type"], db)
        except Exception as err:
            print(err)
        return jsonify({"ranking": -1})

#helper url that simulate the Application functionality
@bp.route('/sign-request', methods=(['POST', 'GET']))
def app_update():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            #get the private key
            private_key = str(request_data['private_key'])

            #encode the given json in base64
            request_data_encoded = base64.b64encode(
                str(request_data['request']).replace('\'', '\"').encode('utf-8'))

            #sign the encoded json using the private key and encode the signature in base64
            signature = auth.sign_message(private_key, request_data_encoded)
            signature_encoded = base64.b64encode(signature)
            #return  {"request":"<encoded json>.<encoded_signature>"}
            return jsonify({"request": f"{request_data_encoded.decode('utf-8')}.{signature_encoded.decode('utf-8')}"})

        except Exception as err:
            return jsonify({"error": str(err.with_traceback(None))})

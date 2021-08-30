import json
import pandas as pd
from datetime import datetime
from collections import Counter

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

fn = r'data.json'
c= Counter()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_year = db.Column(db.String(5), unique=False, nullable=False)
    date_month = db.Column(db.String(3), unique=False, nullable=False)
    date_day = db.Column(db.String(3), unique=False, nullable=False)
    date_time = db.Column(db.String(9), unique=False, nullable=False)
    venue_name = db.Column(db.String(100), unique=False, nullable=False)
    city = db.Column(db.String(30), unique=False, nullable=True)
    country = db.Column(db.String(30), unique=False, nullable=True)
    virtual = db.Column(db.Integer, unique=False, nullable=True)

    def __init__(self,id,date,venue,city,country,virtual) -> None:
        dt = datetime.strptime(date,"%Y-%m-%dT%H:%M:%S")
        self.id =id
        self.date_year,self.date_month,self.date_day =dt.year,dt.month,dt.day
        self.date_time = dt.ctime()
        self.venue_name = venue
        self.city = city
        self.country = country
        self.virtual = virtual


@app.route('/not-usa')
def hello():
    output = []
    for entry in Entry.query.filter(Entry.country!="United States").all():
        output.append(entry)
    return render_template('view.html', entries=output)



@app.route('/aggr')
def aggr():
    return render_template('aggr.html', entries=get_data())

def get_data():
    global c 
    print("hi")
    entries = Entry.query.all()
    for entry in entries:
        c[f"{entry.date_month}/{entry.date_year}"] += 1
    return c

if __name__ == '__main__':
    app.run(debug=True,use_debugger=True)
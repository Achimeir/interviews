from typing import ByteString, Tuple
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def create_keys() -> Tuple[RSA._RSAobj, RSA._RSAobj]:
    # create private and public key using RSA 2048
    private_key = RSA.generate(2048)
    public_key = private_key.publickey()
    return private_key, public_key


def sign_message(private_key, message) -> ByteString:
    # sign the message using the private key and return the signature
    key = RSA.import_key(private_key)
    h = SHA256.new(message)
    sig = pkcs1_15.new(key).sign(h)
    return sig


def verify_signature(public_key, message, signature) -> bool:
    # check if the signature of the data correspond to the public key
    key = RSA.import_key(public_key)
    h = SHA256.new(message.encode('utf-8'))
    try:
        pkcs1_15.new(key).verify(h, signature)
        print("The signature is valid.")
        return True

    except (ValueError, TypeError) as err:
        print(str(err), "The signature is not valid.")
    return False

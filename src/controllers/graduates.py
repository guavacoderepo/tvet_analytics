from flask import Blueprint, jsonify
from src.modules.mongo import create_dummy
from time import sleep


graduates = Blueprint("gradustes", __name__, url_prefix="/api/v1/graduates")


# generate dummy endpoint
@graduates.route("/dummy", methods = ["GET"])
def generate_dummy():
    i = 0

    while i<1000:

        create_dummy()

        i+=1

        sleep(0.5) 
        
        
    return "welcome dummy to dummy generator"





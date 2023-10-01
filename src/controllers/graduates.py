from flask import Blueprint, jsonify


graduates = Blueprint("gradustes", __name__, url_prefix="/api/v1/graduates")


# generate dummy endpoint
@graduates.route("/dummy", methods = ["GET"])
def generate_dummy():
    return "welcome dummy to dummy generator"





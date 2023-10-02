from flask import Blueprint, jsonify
from src.modules.mongo import create_dummy, fetch_all
from time import sleep
from bson.json_util import dumps, loads
from src.utils.geopolicalZones import searchGeopolicalZone


graduates = Blueprint("gradustes", __name__, url_prefix="/api/v1/graduates")


# generate dummy endpoint
@graduates.route("/dummy", methods = ["GET"])
def generate_dummy():
    i = 0

    while i<1000:

        create_dummy()

        i+=1

        sleep(0.5) 
            
    return "welcome dummy!!  Dummy generator done"


# The gender composition of all graduates.(pie chart) graduates vs gender

@graduates.route("/gender/composition", methods = ["GET"])
def gender_composition():

    data = fetch_all()

    load_data = loads(dumps(data))

    total = len(load_data)

    male = len([ gender for gender in load_data if gender["gender"] == "male"])
    female = len([ gender for gender in load_data if gender["gender"] == "female"])
    other = len([ gender for gender in load_data if gender["gender"] == "other"])

   
    return jsonify({
        "status": True,
        "type": "pie chart",
        "unit":"percentage",
        "data":{
            "male": (male/total)*100,
            "female": (female/total)*100,
            "others": (other/total)*100,
        }
    })


# Employment status by geopolitical zones

@graduates.route("/employment/geopolitical", methods = ["GET"])
def employment_by_geopolicalzone():

    data = fetch_all()

    load_data = loads(dumps(data))

    North_Central = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North Central"])
    North_East = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North East"])
    North_West = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North West"])
    South_East = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South East"])
    South_South = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South South"])
    South_West = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South West"])

    North_Central_y = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North Central"  and zone["is_employed"]==True])
    North_East_y = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North East" and zone["is_employed"]==True])
    North_West_y = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North West" and zone["is_employed"]==True])
    South_East_y = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South East" and zone["is_employed"]==True])
    South_South_y = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South South" and zone["is_employed"]==True])
    South_West_y = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South West" and zone["is_employed"]==True])


    return jsonify({
        "status": True,
        "type": "Composite bar chart",
        "unit":"number",
        "data":{
            "North_Central": {
                "emplyed": North_Central_y,
                "unemployed":North_Central-North_Central_y,
                "sum":North_Central,
                }, 
            "North_East": {
                "emplyed": North_East_y,
                "unemployed":North_East-North_East_y,
                "sum": North_East,
            },
            "North_West": {
                "emplyed": North_West_y,
                "unemployed":North_West-North_West_y,
                "sum": North_West,
            },
            "South_East": {
                "emplyed": South_East_y,
                "unemployed":South_East-South_East_y,
                "sum": South_East,
            },
            "South_South": {
                "emplyed": South_South_y,
                "unemployed":South_South-South_South_y,
                "sum": South_South,
            }, 
            "South_West": {
                "emplyed": South_West_y,
                "unemployed":South_West-South_West_y,
                "sum": South_West,
            },   
        }
    })



# Regions with least and highest number of graduates

@graduates.route("/regions", methods = ["GET"])
def Regions_least_and_highest_number_of_graduates():

    data = fetch_all()

    load_data = loads(dumps(data))

    North_Central = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North Central"])
    North_East = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North East"])
    North_West = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "North West"])
    South_East = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South East"])
    South_South = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South South"])
    South_West = len([ zone for zone in load_data if searchGeopolicalZone(zone["state"])  == "South West"])

   
    return jsonify({
        "status": True,
        "type": "no chart",
        "unit":"number",
        "data":{
            "North_Central": North_Central,
            "North_East": North_East,
            "North_West": North_West,
            "South_East": South_East,
            "South_South": South_South,
            "South_West": South_West,
        }
    })




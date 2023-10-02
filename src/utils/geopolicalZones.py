geoPoliticalZones = {
    "North Central": ["benue", "abuja", "kogi", "kwara", "nasarawa", "niger", "plateau"], 

    "North East":  ["adamawa", "bauchi", "borno", "gombe", "taraba", "yobe"], 


    "North West":  ["kaduna", "katsina", "kano", "kebbi", "sokoto", "jigawa", "zamfara"], 


    "South East":  ["abia", "anambra", "ebonyi", "enugu", "imo"], 


    "South South":  ["akwa Ibom", "bayelsa", "cross river", "delta", "edo", "rivers"],

    "South West": ["ekiti", "lagos", "osun", "ondo", "ogun", "oyo"]
}


def searchGeopolicalZone(state):
    for k,v in geoPoliticalZones.items():
        if state in v:
            return k
            break





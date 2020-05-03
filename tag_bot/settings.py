import json


def getConfig():
    f = open(".config.json", "r")
    configRaw = f.read()
    config = json.loads(configRaw)
    return (config["client_id"], config["client_secret"], config["username"], config["password"])

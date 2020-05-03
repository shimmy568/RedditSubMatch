import os
from dotenv import load_dotenv

load_dotenv("./.env", verbose=True)


def getEnv():
    client_id = os.environ.get("TAG_BOT_CLIENT_ID")
    client_secret = os.environ.get("TAG_BOT_CLIENT_SECRET")
    username = os.environ.get("TAG_BOT_USERNAME")
    password = os.environ.get("TAG_BOT_PASSWORD")

    if (not client_id) or (not client_secret) or (not username) or (not password):
        print(
            "You are missing one of the required environment variables to run this script"
        )
        quit()

    return (client_id, client_secret, username, password)

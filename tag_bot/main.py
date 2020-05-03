import re
import pdb
import praw
import settings
from time import sleep


def createConnection(client_id, client_secret, username, password):
    user_agent = f"script:com.tag_bot:v0.0.1 (by u/shimmy568)"
    return praw.Reddit(client_id=client_id,
                       client_secret=client_secret,
                       user_agent=user_agent,
                       username=username,
                       password=password)


def run(r):
    while True:
        print("printing mentions")
        for mention in r.inbox.mentions():
            print(mention)
        sleep(5)   # get_mentions() is non-blocking.


client_id, client_secret, username, password = settings.getConfig()
reddit = createConnection(client_id, client_secret, username, password)
run(reddit)

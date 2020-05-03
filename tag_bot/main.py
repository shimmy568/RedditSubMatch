import re
import pdb
import praw
import settings


def createConnection(client_id, client_secret, username, password):
    user_agent = f"script:com.tag_bot:v0.0.1 (by u/shimmy568)"
    return praw.Reddit(client_id='my client id',
                       client_secret='my client secret',
                       user_agent='my user agent')


def run(reddit):
    while True:
        for mention in r.get_mentions():
            print(mention)
        sleep(5)   # get_mentions() is non-blocking.


client_id, client_secret, username, password = settings.getEnv()
reddit = createConnection(client_id, client_secret, username, password)
run(reddit)

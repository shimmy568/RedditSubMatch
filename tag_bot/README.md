# Tag Bot code

Tag bot is designed to reply to posts that tag this bot with general information about /r/submatch and the bot itself

# Setup

Create a file named `.env` in this directory with the following format:

```bash
TAG_BOT_CLIENT_ID=""
TAG_BOT_CLIENT_SECRET=""
TAG_BOT_USERNAME=""
TAG_BOT_PASSWORD=""
```

Fill in the empty strings with the required information.

Then run

```bash
pip3 install -r requirements.txt
```

And then you should be able to run the script via:

```bash
python3 main.py
```

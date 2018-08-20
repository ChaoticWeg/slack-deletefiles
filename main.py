from dotenv import load_dotenv
from slack import Client

import os

def run():
    token  = os.environ['SLACK_TOKEN']
    client = Client(token)
    client.get_files()

if __name__ == "__main__":
    load_dotenv()
    run()

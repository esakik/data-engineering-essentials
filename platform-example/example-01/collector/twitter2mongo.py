import argparse
import datetime
import json
import os
import time
from os.path import join, dirname

import pymongo
import requests_oauthlib
import tqdm
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# command line options
parser = argparse.ArgumentParser(description='insert data from twitter to mongo db.')
parser.add_argument('-k', '--keyword', type=str, required=True, help="keyword for twitter search")
parser.add_argument('--max_counts', type=int, default=1000, help="max counts to insert")
args = parser.parse_args()

ON_DOCKER = os.environ.get("ON_DOCKER")
KEYWORD = args.keyword
MAX_COUNTS = args.max_counts

# twitter api info
TWITTER_API_URI = "https://stream.twitter.com/1.1/statuses/filter.json"
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN_KEY = os.environ.get("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# mongo db connection info
MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_HOST = "mongo" if ON_DOCKER else "127.0.0.1"
MONGO_PORT = 27017


def main():
    twitter = requests_oauthlib.OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

    while True:
        r = twitter.post(TWITTER_API_URI, data=dict(track=KEYWORD), stream=True)

        status_code = r.status_code
        if status_code == 200:
            break
        elif r.status_code == 420:
            time.sleep(60)
            print(f"Wait 60s for {r.reason}")
        else:
            r.raise_for_status()

    mongo = pymongo.MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}")

    count = 0
    for line in tqdm.tqdm(r.iter_lines(), unit="tweets", mininterval=1):
        if line:
            tweet = json.loads(line)
            tweet["timestamp"] = datetime.datetime.utcnow().isoformat()
            tweet["keyword"] = KEYWORD
            mongo.twitter.sample.insert_one(tweet)

            count += 1

        if MAX_COUNTS <= count:
            break


if __name__ == '__main__':
    main()

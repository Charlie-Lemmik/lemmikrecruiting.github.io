import tweepy
import os
import sys
from dotenv import load_dotenv

# Load keys
load_dotenv(".env.twitter")

# Configure Twitter
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

def post_tweet(text):
    if not text or len(text) < 10:
        print("Error: Tweet too short")
        return
    try:
        response = client.create_tweet(text=text)
        print(f"Posted! ID: {response.data['id']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        post_tweet(sys.argv[1])
    else:
        print("Error: No text provided")

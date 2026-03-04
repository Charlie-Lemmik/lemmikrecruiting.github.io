import tweepy
import os
from dotenv import load_dotenv

# Load keys from .env.twitter
load_dotenv(".env.twitter")

api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate
client = tweepy.Client(
    consumer_key=api_key, consumer_secret=api_secret,
    access_token=access_token, access_token_secret=access_secret
)

# Post Tweet
response = client.create_tweet(text="Hello World! 🏗️ Lemmik Recruiting Services is officially live. Disrupting the construction industry with 15% fees. #Construction #Recruiting #Hiring")

print(f"Tweet posted! ID: {response.data['id']}")

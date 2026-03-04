#!/usr/bin/env python3

import tweepy
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env.panthers file
load_dotenv('.env.panthers')

def post_tweet(tweet_text):
    try:
        # Get Twitter API credentials from environment
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET') 
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        
        if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
            print("❌ Missing Twitter API credentials in .env.panthers file")
            return False
        
        # Initialize Twitter API client
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True
        )
        
        # Post the tweet
        response = client.create_tweet(text=tweet_text)
        
        if response.data:
            print(f"✅ Panthers tweet posted successfully!")
            print(f"📝 Content: {tweet_text}")
            print(f"🔗 Tweet ID: {response.data['id']}")
            return True
        else:
            print("❌ Failed to post Panthers tweet")
            return False
            
    except Exception as e:
        print(f"❌ Error posting Panthers tweet: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python post_panthers.py \"Your tweet text here\"")
        sys.exit(1)
    
    tweet_text = sys.argv[1]
    
    if len(tweet_text) > 280:
        print(f"❌ Tweet too long: {len(tweet_text)} characters (max 280)")
        sys.exit(1)
    
    success = post_tweet(tweet_text)
    sys.exit(0 if success else 1)
import tweepy
import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

# Load keys
load_dotenv(".env.twitter")
load_dotenv(".env")  # Load Gemini API Key

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configure Twitter
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

def generate_tweet():
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = """
    Write a single, engaging tweet for 'Lemmik Recruiting Services', a construction recruiting firm.
    Topic options (pick one):
    1. A quick tip for construction managers about hiring skilled labor.
    2. A brief comment on current construction industry trends (materials, labor shortage, technology).
    3. A motivational quote for contractors.
    
    Constraints:
    - Under 280 characters.
    - Professional but conversational tone.
    - Use 1-2 emojis.
    - Include hashtags like #Construction #Hiring #LemmikRecruits.
    - Do NOT include 'Here is a tweet:' or quotes. Just the tweet text.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def post_tweet():
    try:
        tweet_text = generate_tweet()
        print(f"Generated Tweet: {tweet_text}")
        
        response = client.create_tweet(text=tweet_text)
        print(f"Posted! ID: {response.data['id']}")
        
        # Log it
        with open("tweet_log.txt", "a") as f:
            f.write(f"{datetime.now()}: {tweet_text}\n")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    post_tweet()

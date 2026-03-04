#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import anthropic

# Load environment variables
load_dotenv('.env.gmail')

def test_anthropic_credits():
    """Test Anthropic API connectivity and verify credits"""
    
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ Missing ANTHROPIC_API_KEY in .env.gmail")
        return
    
    print("🔑 Found API key. Testing connection...")
    
    try:
        client = anthropic.Anthropic(api_key=api_key)
        
        # Try a very small, cheap request
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=10,
            messages=[
                {"role": "user", "content": "Hello"}
            ]
        )
        
        print("\n✅ SUCCESS! Anthropic API is working.")
        print(f"🤖 Model used: {message.model}")
        print(f"💬 Response: {message.content[0].text}")
        print("\n💰 Credits are active and available!")
        
    except anthropic.AuthenticationError:
        print("\n❌ Authentication Error: Invalid API key.")
    except anthropic.PermissionError:
        print("\n❌ Permission Error: Account unauthorized or credits empty.")
    except anthropic.RateLimitError:
        print("\n❌ Rate Limit Error: Too many requests (or empty credits).")
    except anthropic.APIError as e:
        print(f"\n❌ API Error: {e}")
        if "credit balance is too low" in str(e).lower():
            print("   -> CONFIRMED: Still seeing 'credit balance too low' error.")
            print("   -> It might take a few minutes for credits to propagate.")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")

if __name__ == "__main__":
    test_anthropic_credits()

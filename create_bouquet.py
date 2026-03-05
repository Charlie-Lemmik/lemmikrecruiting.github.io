#!/usr/bin/env python3

import requests
from PIL import Image, ImageDraw, ImageFont
import os

def create_bouquet():
    print("🌸 Creating beautiful bouquet image...")
    
    try:
        # Download a beautiful bouquet image from Unsplash
        bouquet_url = "https://images.unsplash.com/photo-1590736969955-71cc94901144?q=80&w=800&auto=format&fit=crop"
        response = requests.get(bouquet_url)
        
        with open("beautiful_bouquet.jpg", "wb") as f:
            f.write(response.content)
            
        print("✅ Beautiful bouquet image created!")
        return "beautiful_bouquet.jpg"
        
    except Exception as e:
        print(f"❌ Error creating bouquet: {e}")
        return None

if __name__ == "__main__":
    create_bouquet()
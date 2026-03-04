#!/usr/bin/env python3

import os
import requests
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

def create_twitter_assets():
    print("🎨 Starting Twitter Asset Generation...")
    
    # 1. PROFILE PICTURE (Square Crop of Logo)
    try:
        logo_path = "lemmik_logo_robot_v2.jpg"
        if os.path.exists(logo_path):
            img = Image.open(logo_path)
            
            # Create a white square background
            square_size = 500
            profile_pic = Image.new("RGB", (square_size, square_size), "white")
            
            # Calculate resize to fill most of the space (minimal padding)
            # Keep aspect ratio but make it bigger
            img.thumbnail((480, 480), Image.Resampling.LANCZOS)
            
            # Center the logo
            x_offset = (square_size - img.width) // 2
            y_offset = (square_size - img.height) // 2
            
            profile_pic.paste(img, (x_offset, y_offset))
            profile_pic.save("twitter_profile.jpg", quality=95)
            print("✅ Created: twitter_profile.jpg")
        else:
            print("❌ Error: Logo file not found!")
    except Exception as e:
        print(f"❌ Error creating profile pic: {e}")

    # 2. BANNER IMAGE (Matching Website Hero)
    try:
        # Download the website hero image
        hero_url = "https://images.unsplash.com/photo-1504307651254-35680f356dfd?q=80&w=2000&auto=format&fit=crop"
        response = requests.get(hero_url)
        
        with open("temp_hero.jpg", "wb") as f:
            f.write(response.content)
            
        hero = Image.open("temp_hero.jpg")
        
        # Crop/Resize to Twitter Banner specs (1500x500)
        # We want the center-ish part of the image
        target_w, target_h = 1500, 500
        
        # Resize preserving aspect ratio (width based)
        aspect = hero.height / hero.width
        new_h = int(target_w * aspect)
        hero = hero.resize((target_w, max(new_h, target_h)), Image.Resampling.LANCZOS)
        
        # Crop vertical center
        crop_y = (hero.height - target_h) // 2
        banner = hero.crop((0, crop_y, target_w, crop_y + target_h))
        
        # Apply Navy Blue Overlay (Brand Color)
        overlay = Image.new("RGB", banner.size, "#0f172a") # Dark Navy
        banner = Image.blend(banner, overlay, 0.75) # 75% opacity overlay
        
        # Add Text
        draw = ImageDraw.Draw(banner)
        
        # Try to load a font, fallback to default
        try:
            # Linux paths for fonts
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)
            sub_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
        except:
            title_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
            print("⚠️ Warning: Using default font")

        # Text 1: LEMMIK RECRUITING
        text1 = "LEMMIK RECRUITING"
        # Calculate text position (Centered)
        # Note: PIL default font doesn't support getbbox well, but TTF does
        try:
            _, _, w1, h1 = draw.textbbox((0, 0), text1, font=title_font)
            x1 = (target_w - w1) // 2
            y1 = (target_h - h1) // 2 - 30
            draw.text((x1, y1), text1, font=title_font, fill="white")
            
            # Text 2: Tagline
            text2 = "Fully Automated. Flat $5,000 Fee."
            _, _, w2, h2 = draw.textbbox((0, 0), text2, font=sub_font)
            x2 = (target_w - w2) // 2
            y2 = y1 + h1 + 20
            # Use Safety Orange color for the fee part
            draw.text((x2, y2), text2, font=sub_font, fill="#fbbf24") 
            
        except AttributeError:
            # Fallback for very old PIL versions
            draw.text((100, 200), text1, fill="white")
            draw.text((100, 300), text2, fill="yellow")

        banner.save("twitter_banner.jpg", quality=95)
        print("✅ Created: twitter_banner.jpg")
        
        # Cleanup
        if os.path.exists("temp_hero.jpg"):
            os.remove("temp_hero.jpg")
            
    except Exception as e:
        print(f"❌ Error creating banner: {e}")

if __name__ == "__main__":
    create_twitter_assets()

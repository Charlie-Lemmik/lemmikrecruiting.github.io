#!/usr/bin/env python3
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv('.env.gmail')
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

print("🚀 Attempting SINGLE logo generation...", flush=True)

try:
    model = genai.GenerativeModel('nano-banana-pro-preview')
    response = model.generate_content(
        "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Deep Navy Blue and Metallic Silver color scheme. A sophisticated circular emblem containing a detailed city skyline silhouette with crane elements. Modern, trustworthy, corporate aesthetic. White background. Vector style with shading.",
        generation_config=genai.types.GenerationConfig(temperature=0.7)
    )
    
    # Check for image data
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                filename = "logo_single_test_navy.jpg"
                with open(filename, 'wb') as f:
                    f.write(part.inline_data.data)
                print(f"✅ SUCCESS! Saved: {filename} ({os.path.getsize(filename)} bytes)", flush=True)
                exit(0)
    
    print("❌ No image data returned.", flush=True)

except Exception as e:
    print(f"❌ Error: {e}", flush=True)

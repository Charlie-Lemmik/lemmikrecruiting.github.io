#!/usr/bin/env python3

import os
import sys
# Print immediately to show life
print("🚀 Script starting...", flush=True)

try:
    import google.generativeai as genai
    from dotenv import load_dotenv
    print("✅ Libraries imported", flush=True)
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

# Load environment variables
load_dotenv('.env.gmail')

def create_single_detailed_logo():
    """Create just one detailed logo to test connection"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    print("🔑 API Configured", flush=True)
    
    model = genai.GenerativeModel('nano-banana-pro-preview')
    
    # Prompt for the first detailed concept (Navy/Silver Skyline)
    prompt = "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Deep Navy Blue and Metallic Silver color scheme. A sophisticated circular emblem containing a detailed city skyline silhouette with crane elements. Modern, trustworthy, corporate aesthetic. White background. Vector style with shading."
    
    print("🎨 Generating Navy Skyline Logo...", flush=True)
    
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.9,
                max_output_tokens=2048,
            )
        )
        
        # Extract image data
        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'content') and candidate.content.parts:
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data') and part.inline_data and part.inline_data.data:
                        
                        image_data = part.inline_data.data
                        mime_type = part.inline_data.mime_type
                        
                        ext = 'jpg'
                        if 'png' in mime_type:
                            ext = 'png'
                        
                        filename = f"detailed_logo_01_Navy_Skyline.{ext}"
                        
                        with open(filename, 'wb') as f:
                            f.write(image_data)
                        
                        file_size = os.path.getsize(filename)
                        print(f"✅ SAVED: {filename} ({file_size/1024:.1f} KB)", flush=True)
                        return True
                else:
                    print("❌ No image data found in response", flush=True)
            else:
                print("❌ No content parts in response", flush=True)
        else:
            print("❌ No candidates in response", flush=True)
            
    except Exception as e:
        print(f"❌ Error creating logo: {e}", flush=True)
        return False

if __name__ == "__main__":
    create_single_detailed_logo()

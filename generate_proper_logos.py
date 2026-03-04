#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv('.env.gmail')

def generate_logos_with_imagen():
    """Use proper image generation models to create logos"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    # Logo prompts based on Nano Banana Pro concepts
    logo_concepts = [
        {
            "name": "Rising_Cityscape",
            "prompt": "Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) color scheme. Clean circular border with three vertical building bars of different heights inside representing city skyline. Simple geometric design. White background. Corporate Fortune 500 style."
        },
        {
            "name": "Keystone_Bridge",
            "prompt": "Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) color. Circular border containing abstract bridge arch with central keystone block. Clean geometric construction theme. White background. Corporate style."
        },
        {
            "name": "Industrial_Compass", 
            "prompt": "Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) color. Circular border with geometric compass/caliper engineering tool. Precision and construction theme. Clean simple design. White background."
        },
        {
            "name": "Growth_Arrow",
            "prompt": "Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) color. Circular border containing building blocks arranged to form upward arrow. Growth and progress theme. Simple geometric shapes. White background."
        },
        {
            "name": "Steel_Beam_L",
            "prompt": "Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) color. Circular border with industrial I-beam shaped like letter 'L' for Lemmik. Heavy construction theme. Simple strong design. White background."
        }
    ]
    
    print("🎨 Generating Professional Logos with Google Imagen...")
    print("🌲 Forest Green Construction Recruiting Logos")
    print("=" * 60)
    
    # Try different image generation models
    image_models = [
        'imagen-4.0-generate-001',
        'imagen-4.0-ultra-generate-001', 
        'gemini-2.0-flash-exp-image-generation'
    ]
    
    successful_logos = []
    
    for model_name in image_models:
        print(f"\n🧪 Trying model: {model_name}")
        
        try:
            model = genai.GenerativeModel(model_name)
            
            for i, concept in enumerate(logo_concepts, 1):
                print(f"  🎯 Generating: {concept['name']}")
                
                try:
                    response = model.generate_content(concept['prompt'])
                    
                    # Check for image data in response
                    if hasattr(response, 'candidates') and response.candidates:
                        candidate = response.candidates[0]
                        if hasattr(candidate, 'content') and candidate.content.parts:
                            for part in candidate.content.parts:
                                if hasattr(part, 'inline_data') and part.inline_data:
                                    # Found image data!
                                    image_data = part.inline_data.data
                                    mime_type = part.inline_data.mime_type
                                    
                                    # Determine file extension
                                    if 'png' in mime_type:
                                        ext = 'png'
                                    elif 'jpeg' in mime_type or 'jpg' in mime_type:
                                        ext = 'jpg'
                                    else:
                                        ext = 'png'  # default
                                    
                                    filename = f"professional_logo_{i}_{concept['name']}.{ext}"
                                    
                                    # Save image
                                    with open(filename, 'wb') as f:
                                        f.write(base64.b64decode(image_data))
                                    
                                    print(f"    ✅ Saved: {filename}")
                                    successful_logos.append(filename)
                                    break
                            else:
                                print(f"    ⚠️  No image data in response")
                        else:
                            print(f"    ⚠️  No content in response")
                    else:
                        print(f"    ⚠️  No candidates in response")
                        
                except Exception as e:
                    print(f"    ❌ Error with {concept['name']}: {e}")
                    continue
                    
        except Exception as e:
            print(f"  ❌ Model {model_name} failed: {e}")
            continue
    
    print("\n" + "=" * 60)
    if successful_logos:
        print(f"🎯 SUCCESS! Generated {len(successful_logos)} professional logos!")
        print("\n📁 Created files:")
        for logo in successful_logos:
            print(f"   - {logo}")
        print(f"\n🌲 All logos use forest green (#1E5128) with professional corporate styling!")
    else:
        print("❌ No logos were successfully generated.")
        print("💡 The models might not support image generation or need different parameters.")

def test_simple_image_generation():
    """Test simple image generation first"""
    print("\n🧪 Testing simple image generation...")
    
    api_key = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=api_key)
    
    try:
        # Try the most promising model
        model = genai.GenerativeModel('imagen-4.0-generate-001')
        
        simple_prompt = "A simple green circle on white background"
        
        response = model.generate_content(simple_prompt)
        print(f"Response type: {type(response)}")
        print(f"Response text (if any): {getattr(response, 'text', 'No text')}")
        
        # Check structure
        if hasattr(response, 'candidates'):
            print(f"Candidates: {len(response.candidates)}")
            if response.candidates:
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and candidate.content.parts:
                    print(f"Parts: {len(candidate.content.parts)}")
                    for i, part in enumerate(candidate.content.parts):
                        print(f"  Part {i}: {type(part)}")
                        if hasattr(part, 'inline_data'):
                            print(f"    Has inline_data: {part.inline_data is not None}")
        
    except Exception as e:
        print(f"Simple test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_simple_image_generation()
    generate_logos_with_imagen()
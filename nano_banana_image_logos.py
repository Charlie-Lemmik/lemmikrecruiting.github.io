#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv('.env.gmail')

def generate_logo_images_with_nano_banana():
    """Use Nano Banana Pro to generate actual logo images"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    logo_prompts = [
        {
            "name": "Rising Cityscape",
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Clean circular frame with three vertical building bars of different heights inside, like a city skyline. Minimalist, geometric, Fortune 500 style. White background."
        },
        {
            "name": "Keystone Bridge", 
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame containing an abstract bridge arch with a keystone block at the center. Clean, geometric design. Construction industry theme. White background."
        },
        {
            "name": "Construction Compass",
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame with geometric compass/caliper tool inside. Engineering precision theme. Clean, minimalist design. White background."
        },
        {
            "name": "Growth Arrow",
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame containing modular building blocks forming an upward arrow. Growth and progress theme. Clean geometric shapes. White background."
        },
        {
            "name": "I-Beam Monogram",
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame with industrial I-beam shaped like letter 'L'. Heavy construction, industrial strength theme. Minimalist design. White background."
        },
        {
            "name": "Blueprint Grid",
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame containing architectural blueprint grid with center target point. Planning and precision theme. Clean lines. White background."
        },
        {
            "name": "Bridge Connection",
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame with suspension bridge design. Infrastructure and connection theme. Simple, professional appearance. White background."
        },
        {
            "name": "Tower Crane",
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame containing abstract tower crane silhouette. Construction power theme. Clean, geometric design. White background."
        },
        {
            "name": "Team Structure", 
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame with geometric human figure made of building blocks. People and construction theme. Minimalist design. White background."
        },
        {
            "name": "Quality Shield",
            "prompt": "Professional logo for LEMMIK CONSTRUCTION RECRUITING. Forest green (#1E5128) color. Circular frame containing gear-shield hybrid shape with diamond center. Industrial reliability theme. Professional appearance. White background."
        }
    ]
    
    try:
        model = genai.GenerativeModel('nano-banana-pro-preview')
        
        print("🍌 Using Nano Banana Pro for IMAGE Generation...")
        print("🌲 Creating professional forest green logos...")
        print("=" * 70)
        
        created_logos = []
        
        for i, logo_data in enumerate(logo_prompts, 1):
            print(f"🎨 Generating Logo {i}: {logo_data['name']}")
            
            try:
                # Generate image with Nano Banana Pro
                response = model.generate_content(logo_data['prompt'])
                
                # Check if response contains image data
                if hasattr(response, 'candidates') and response.candidates:
                    candidate = response.candidates[0]
                    
                    # Check for image parts
                    if hasattr(candidate, 'content') and candidate.content.parts:
                        for part in candidate.content.parts:
                            if hasattr(part, 'inline_data') and part.inline_data:
                                # Save image data
                                image_data = part.inline_data.data
                                filename = f"nano_generated_logo_{i}_{logo_data['name'].lower().replace(' ', '_')}.png"
                                
                                with open(filename, 'wb') as f:
                                    f.write(base64.b64decode(image_data))
                                
                                print(f"✅ Saved: {filename}")
                                created_logos.append(filename)
                                break
                        else:
                            print(f"⚠️  No image data found in response for {logo_data['name']}")
                    else:
                        print(f"⚠️  No content parts in response for {logo_data['name']}")
                else:
                    # Handle text response (might need different approach)
                    print(f"📝 Response for {logo_data['name']}: {response.text[:100]}...")
                    
            except Exception as e:
                print(f"❌ Error generating {logo_data['name']}: {e}")
                continue
        
        print("=" * 70)
        if created_logos:
            print(f"🎯 Successfully created {len(created_logos)} logo images!")
            print("\n📁 Generated files:")
            for logo in created_logos:
                print(f"   - {logo}")
        else:
            print("⚠️  No image files were created. Nano Banana Pro might not support image generation in this way.")
            print("\n💡 Let me try a different approach...")
            
            # Alternative: Try with different model parameters
            try_alternative_approach()
            
    except Exception as e:
        print(f"❌ Error with Nano Banana Pro: {e}")
        print("\n💡 Let me investigate available image generation capabilities...")
        investigate_image_models()

def try_alternative_approach():
    """Try alternative approach for image generation"""
    print("\n🔄 Trying alternative approach...")
    
    try:
        # Check if there's a different way to call image generation
        model = genai.GenerativeModel('nano-banana-pro-preview')
        
        prompt = "Generate a professional logo image for LEMMIK CONSTRUCTION RECRUITING in forest green"
        
        # Try different generation parameters
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.8,
                top_k=40,
                max_output_tokens=1024,
            )
        )
        
        print("Alternative response:", response.text[:200])
        
    except Exception as e:
        print(f"Alternative approach also failed: {e}")

def investigate_image_models():
    """Check what models are available and their capabilities"""
    print("\n🔍 Investigating available models...")
    
    try:
        api_key = os.getenv('GOOGLE_API_KEY')
        genai.configure(api_key=api_key)
        
        models = genai.list_models()
        print("\n📋 Available models:")
        
        image_capable = []
        
        for model in models:
            model_name = model.name
            print(f"   - {model_name}")
            
            # Check if model might support images
            if any(keyword in model_name.lower() for keyword in ['image', 'vision', 'banana', 'generate']):
                print(f"     *** Potentially image capable ***")
                image_capable.append(model_name)
                
                # Try to get model info
                try:
                    supported_methods = model.supported_generation_methods
                    print(f"     Supported methods: {supported_methods}")
                except:
                    pass
        
        if image_capable:
            print(f"\n🎨 Found {len(image_capable)} potentially image-capable models:")
            for model in image_capable:
                print(f"   - {model}")
        else:
            print("\n⚠️  No clearly image-capable models found.")
            
    except Exception as e:
        print(f"Error investigating models: {e}")

if __name__ == "__main__":
    generate_logo_images_with_nano_banana()
#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv('.env.gmail')

def try_nano_banana_image_generation():
    """Try different approaches with Nano Banana Pro for image generation"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    print("🍌 Testing Nano Banana Pro for Image Generation...")
    print("=" * 50)
    
    try:
        model = genai.GenerativeModel('nano-banana-pro-preview')
        
        # Try different prompt formats that might trigger image generation
        image_prompts = [
            "Generate an image: Professional logo for LEMMIK CONSTRUCTION RECRUITING in forest green color",
            "Create image: Simple circular logo with forest green building bars, white background",
            "Image generation prompt: Minimalist construction company logo, forest green (#1E5128), circular frame",
            "[IMAGE] Professional logo design for construction recruiting company, forest green theme",
            "GENERATE_IMAGE: Clean geometric logo with forest green color scheme for LEMMIK CONSTRUCTION RECRUITING",
        ]
        
        for i, prompt in enumerate(image_prompts, 1):
            print(f"\n🧪 Test {i}: Trying prompt format...")
            print(f"   Prompt: {prompt[:80]}...")
            
            try:
                # Try with different generation parameters
                response = model.generate_content(
                    prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                        top_p=0.9,
                        max_output_tokens=2048,
                    )
                )
                
                print(f"   ✅ Got response type: {type(response)}")
                
                # Check if there's image data
                if hasattr(response, 'candidates') and response.candidates:
                    candidate = response.candidates[0]
                    if hasattr(candidate, 'content') and candidate.content.parts:
                        print(f"   📊 Found {len(candidate.content.parts)} parts")
                        
                        for j, part in enumerate(candidate.content.parts):
                            print(f"      Part {j}: {type(part)}")
                            
                            # Check for inline_data (images)
                            if hasattr(part, 'inline_data') and part.inline_data:
                                print(f"      🎨 FOUND IMAGE DATA!")
                                image_data = part.inline_data.data
                                mime_type = part.inline_data.mime_type
                                
                                print(f"      📁 MIME type: {mime_type}")
                                print(f"      📊 Data length: {len(image_data) if image_data else 0}")
                                
                                if image_data:
                                    # Save the image
                                    filename = f"nano_banana_logo_test_{i}.png"
                                    with open(filename, 'wb') as f:
                                        f.write(base64.b64decode(image_data))
                                    print(f"      ✅ SAVED IMAGE: {filename}")
                                    return filename
                            
                            # Check for text
                            elif hasattr(part, 'text') and part.text:
                                print(f"      📝 Text: {part.text[:100]}...")
                            
                            else:
                                print(f"      ❓ Unknown part type")
                
                # Also check the response text
                if hasattr(response, 'text'):
                    text = response.text
                    print(f"   📝 Response text: {text[:150]}...")
                    
                    # Check if text contains image-related content
                    if any(keyword in text.lower() for keyword in ['image', 'generated', 'logo', 'created']):
                        print(f"   🎯 Response mentions image generation!")
                
            except Exception as e:
                print(f"   ❌ Error with prompt {i}: {e}")
                continue
        
        print("\n" + "=" * 50)
        print("🔍 Detailed Model Investigation...")
        
        # Get more details about Nano Banana Pro
        models = genai.list_models()
        for model_info in models:
            if 'nano-banana-pro' in model_info.name:
                print(f"📋 Model: {model_info.name}")
                print(f"   Supported methods: {model_info.supported_generation_methods}")
                print(f"   Input token limit: {getattr(model_info, 'input_token_limit', 'Unknown')}")
                print(f"   Output token limit: {getattr(model_info, 'output_token_limit', 'Unknown')}")
                
                # Check if it has any special capabilities
                if hasattr(model_info, 'supported_media_types'):
                    print(f"   Supported media: {model_info.supported_media_types}")
                if hasattr(model_info, 'description'):
                    print(f"   Description: {model_info.description}")
                break
        
        print("\n💡 If Nano Banana Pro is supposed to generate images:")
        print("   - The prompts might need a specific format")
        print("   - There might be a different API method")
        print("   - It might require special parameters")
        print("   - The image data might be in a different response field")
        
        return None
        
    except Exception as e:
        print(f"❌ Major error testing Nano Banana Pro: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    result = try_nano_banana_image_generation()
    if result:
        print(f"\n🎉 SUCCESS! Created image: {result}")
    else:
        print(f"\n❌ No images were generated")
        print(f"💭 Nano Banana Pro might be text-only, or require different approach")
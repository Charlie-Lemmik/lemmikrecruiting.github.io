#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv('.env.gmail')

def debug_single_logo():
    """Debug single logo generation to understand the issue"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    print("🔍 Debugging Logo Generation...")
    print("=" * 50)
    
    model = genai.GenerativeModel('nano-banana-pro-preview')
    
    prompt = "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color scheme. Clean circular border frame with three vertical building bars of different heights inside representing modern city skyline. Simple geometric design on white background. Corporate Fortune 500 style logo."
    
    print(f"🎨 Testing prompt: {prompt[:80]}...")
    
    try:
        response = model.generate_content(prompt)
        
        print(f"✅ Response type: {type(response)}")
        print(f"📊 Response attributes: {[attr for attr in dir(response) if not attr.startswith('_')]}")
        
        if hasattr(response, 'candidates') and response.candidates:
            print(f"📋 Number of candidates: {len(response.candidates)}")
            
            candidate = response.candidates[0]
            print(f"🎯 Candidate type: {type(candidate)}")
            
            if hasattr(candidate, 'content') and candidate.content:
                print(f"📄 Content type: {type(candidate.content)}")
                print(f"🧩 Number of parts: {len(candidate.content.parts) if candidate.content.parts else 0}")
                
                if candidate.content.parts:
                    for i, part in enumerate(candidate.content.parts):
                        print(f"\n   Part {i}:")
                        print(f"      Type: {type(part)}")
                        print(f"      Attributes: {[attr for attr in dir(part) if not attr.startswith('_')]}")
                        
                        # Check for inline_data
                        if hasattr(part, 'inline_data') and part.inline_data:
                            print(f"      🎨 HAS INLINE_DATA!")
                            
                            inline_data = part.inline_data
                            print(f"         Type: {type(inline_data)}")
                            print(f"         Attributes: {[attr for attr in dir(inline_data) if not attr.startswith('_')]}")
                            
                            if hasattr(inline_data, 'mime_type'):
                                print(f"         MIME type: {inline_data.mime_type}")
                            
                            if hasattr(inline_data, 'data'):
                                data = inline_data.data
                                print(f"         Data type: {type(data)}")
                                print(f"         Data length: {len(data) if data else 0}")
                                
                                if data:
                                    print(f"         First 50 chars: {str(data)[:50]}")
                                    
                                    # Try to save the raw data first
                                    with open('debug_raw_data.bin', 'wb') as f:
                                        if isinstance(data, str):
                                            # Try base64 decode
                                            try:
                                                decoded = base64.b64decode(data)
                                                f.write(decoded)
                                                print(f"         ✅ Saved raw decoded data: {len(decoded)} bytes")
                                                
                                                # Try to save as image
                                                with open('debug_logo.jpg', 'wb') as img_f:
                                                    img_f.write(decoded)
                                                print(f"         ✅ Saved as debug_logo.jpg")
                                                
                                            except Exception as e:
                                                print(f"         ❌ Base64 decode failed: {e}")
                                                # Save as raw string
                                                f.write(data.encode('utf-8'))
                                        else:
                                            f.write(data)
                                            print(f"         ✅ Saved raw binary data")
                                else:
                                    print(f"         ❌ No data in inline_data")
                        
                        # Check for text
                        elif hasattr(part, 'text') and part.text:
                            print(f"      📝 Text content: {part.text[:100]}...")
                        
                        else:
                            print(f"      ❓ Unknown part content")
            else:
                print(f"❌ No content in candidate")
        else:
            print(f"❌ No candidates in response")
        
        # Also check direct response text
        if hasattr(response, 'text'):
            print(f"\n📝 Direct response text: {response.text[:200]}...")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_single_logo()
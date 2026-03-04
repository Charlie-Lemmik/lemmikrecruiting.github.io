#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env.gmail')

def test_nano_banana_capabilities():
    """Test what Nano Banana Pro can actually do"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    print("🍌 Testing Nano Banana Pro capabilities...")
    print("=" * 50)
    
    try:
        # List available models first
        print("📋 Available models:")
        models = genai.list_models()
        for model in models:
            print(f"   - {model.name}")
            if 'banana' in model.name.lower():
                print(f"     *** This is Nano Banana! ***")
                print(f"     Supported methods: {model.supported_generation_methods}")
    
        print("\n" + "=" * 50)
        
        # Test basic text generation with Nano Banana Pro
        print("🧪 Testing basic Nano Banana Pro functionality...")
        
        model = genai.GenerativeModel('nano-banana-pro-preview')
        
        simple_prompt = "Hello, can you create a simple logo description?"
        
        response = model.generate_content(simple_prompt)
        print(f"✅ Response type: {type(response)}")
        print(f"✅ Response text: {response.text[:200]}...")
        
        # Check response structure
        print(f"\n🔍 Response attributes: {dir(response)}")
        
        if hasattr(response, 'candidates'):
            print(f"📊 Number of candidates: {len(response.candidates)}")
            if response.candidates:
                candidate = response.candidates[0]
                print(f"🎯 Candidate attributes: {dir(candidate)}")
                
                if hasattr(candidate, 'content'):
                    print(f"📄 Content attributes: {dir(candidate.content)}")
                    if hasattr(candidate.content, 'parts'):
                        print(f"🧩 Number of parts: {len(candidate.content.parts)}")
                        for i, part in enumerate(candidate.content.parts):
                            print(f"   Part {i} type: {type(part)}")
                            print(f"   Part {i} attributes: {dir(part)}")
        
    except Exception as e:
        print(f"❌ Error testing Nano Banana Pro: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_nano_banana_capabilities()
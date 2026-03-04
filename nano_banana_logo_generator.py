#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env.gmail')

def test_nano_banana_for_logos():
    """Test Nano Banana Pro model for logo design concepts"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    try:
        # Try Nano Banana Pro model
        model = genai.GenerativeModel('nano-banana-pro-preview')
        
        prompt = """
Create 3 professional logo concept descriptions for "LEMMIK CONSTRUCTION RECRUITING":

Business Context:
- AI-powered executive recruiting firm  
- Specializes in heavy civil construction industry
- Modern, technology-forward approach
- Targets construction companies and skilled professionals
- Premium positioning in the market

For each logo concept, provide:
1. Visual description (icon, layout, style)
2. Color palette with hex codes
3. Typography recommendations
4. Brand personality it conveys
5. Target audience appeal

Make them sophisticated, professional, and memorable. Think Fortune 500 company quality.
        """
        
        print("🍌 Testing Nano Banana Pro for logo concepts...")
        response = model.generate_content(prompt)
        
        print("✅ Nano Banana Pro response:")
        print("=" * 60)
        print(response.text)
        print("=" * 60)
        
        return response.text
        
    except Exception as e:
        print(f"❌ Error with Nano Banana Pro: {e}")
        
        # Fallback to regular Gemini
        try:
            print("\n🔄 Trying fallback to Gemini Pro Latest...")
            model = genai.GenerativeModel('gemini-pro-latest')
            response = model.generate_content(prompt)
            
            print("✅ Gemini Pro Latest response:")
            print("=" * 60)
            print(response.text)
            print("=" * 60)
            
        except Exception as e2:
            print(f"❌ Both models failed: {e2}")

if __name__ == "__main__":
    test_nano_banana_for_logos()
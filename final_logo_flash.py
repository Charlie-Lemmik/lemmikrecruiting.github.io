#!/usr/bin/env python3

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env.gmail')

def create_logos_flash():
    """Create 10 detailed logos using Gemini 1.5 Flash (Higher Limits)"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    # Switching to Flash for higher rate limits
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # The 10 Detailed Concepts
    concepts = [
        ("Navy_Skyline", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Deep Navy Blue and Metallic Silver color scheme. A sophisticated circular emblem containing a detailed city skyline silhouette with crane elements. Modern, trustworthy, corporate aesthetic. White background. Vector style with shading."),
        ("Orange_Helmet", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Construction Safety Orange and Dark Grey color scheme. A stylized, detailed hard hat icon integrated with a gear mechanism. Represents safety and industry workforce. Clean, bold lines. White background."),
        ("Teal_Blueprint", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Architectural Teal and Charcoal color scheme. A detailed rolled blueprint document icon forming a subtle letter 'L'. Precision planning theme. Elegant, professional design. White background."),
        ("Red_Steel", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Brick Red and Steel Grey color scheme. An abstract structural steel framework forming a stable hexagonal shape. Represents strength and foundation. Industrial aesthetic. White background."),
        ("Gold_Handshake", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Metallic Gold and Black color scheme. A stylized handshake icon where the hands are formed from geometric building blocks. Represents partnership and deal-making. Premium, executive feel. White background."),
        ("Green_Bridge", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest Green and Lime Green gradient. A modern cable-stayed bridge design with detailed suspension cables. Represents connecting talent. Dynamic, forward-looking. White background."),
        ("Yellow_Hook", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Industrial Yellow and Black color scheme. A detailed crane hook lifting a cubic block. Represents heavy lifting and placement. Bold, high-contrast design. White background."),
        ("Purple_Tower", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Royal Purple and Silver color scheme. Abstract geometric shapes rising to form a skyscraper. Represents career elevation and executive search. Sophisticated, luxury feel. White background."),
        ("Blue_Compass", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Slate Blue and Copper color scheme. A detailed drafting compass overlaid on a subtle grid background. Represents precision recruiting. Technical, engineering aesthetic. White background."),
        ("Multi_Globe", "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Navy Blue, Green, and Grey multicolor. A stylized globe constructed from interconnected nodes and beams. Represents a wide network of candidates. Global, connected feel. White background.")
    ]
    
    print("⚡ Generating 10 Final Logos with Gemini 1.5 Flash...", flush=True)
    
    for i, (name, prompt) in enumerate(concepts, 1):
        print(f"\n🎨 Generating {i}/10: {name}...", flush=True)
        try:
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    top_p=0.9,
                    max_output_tokens=2048,
                )
            )
            
            # Extract image
            if hasattr(response, 'candidates') and response.candidates:
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and candidate.content.parts:
                    for part in candidate.content.parts:
                        if hasattr(part, 'inline_data') and part.inline_data and part.inline_data.data:
                            image_data = part.inline_data.data
                            mime_type = part.inline_data.mime_type
                            ext = 'png' if 'png' in mime_type else 'jpg'
                            
                            filename = f"logo_flash_{i:02d}_{name}.{ext}"
                            path = os.path.join(os.getcwd(), filename)
                            
                            with open(path, 'wb') as f:
                                f.write(image_data)
                            
                            if os.path.exists(path):
                                size = os.path.getsize(path)
                                print(f"   ✅ SAVED: {filename} ({size/1024:.1f} KB)", flush=True)
                            else:
                                print(f"   ❌ FAILED TO SAVE: {filename}", flush=True)
                            break
                    else:
                        # If no inline_data, check if it generated text instead (Flash sometimes does this)
                        if hasattr(candidate.content.parts[0], 'text'):
                             print(f"   ⚠️ Model returned text instead of image: '{candidate.content.parts[0].text[:50]}...'", flush=True)
                        else:
                             print("   ❌ No image data found", flush=True)
                else:
                    print("   ❌ No content parts", flush=True)
            else:
                print("   ❌ No candidates", flush=True)
                
        except Exception as e:
            print(f"   ❌ Error: {e}", flush=True)

if __name__ == "__main__":
    create_logos_flash()

#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env.gmail')

def create_detailed_logos():
    """Create 10 detailed, varied-color professional logos"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    # Varied concepts with more detail and color
    logo_concepts = [
        {
            "name": "Detailed_Skyline_Blue",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Deep Navy Blue and Metallic Silver color scheme. A sophisticated circular emblem containing a detailed city skyline silhouette with crane elements. Modern, trustworthy, corporate aesthetic. White background. Vector style with shading."
        },
        {
            "name": "Construction_Helmet_Orange", 
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Construction Safety Orange and Dark Grey color scheme. A stylized, detailed hard hat icon integrated with a gear mechanism. Represents safety and industry workforce. Clean, bold lines. White background."
        },
        {
            "name": "Blueprint_Roll_Teal",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Architectural Teal and Charcoal color scheme. A detailed rolled blueprint document icon forming a subtle letter 'L'. Precision planning theme. Elegant, professional design. White background."
        },
        {
            "name": "Steel_Structure_Red",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Brick Red and Steel Grey color scheme. An abstract structural steel framework forming a stable hexagonal shape. Represents strength and foundation. Industrial aesthetic. White background."
        },
        {
            "name": "Handshake_Gold",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Metallic Gold and Black color scheme. A stylized handshake icon where the hands are formed from geometric building blocks. Represents partnership and deal-making. Premium, executive feel. White background."
        },
        {
            "name": "Modern_Bridge_Green",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest Green and Lime Green gradient. A modern cable-stayed bridge design with detailed suspension cables. Represents connecting talent. Dynamic, forward-looking. White background."
        },
        {
            "name": "Crane_Hook_Yellow",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Industrial Yellow and Black color scheme. A detailed crane hook lifting a cubic block. Represents heavy lifting and placement. Bold, high-contrast design. White background."
        },
        {
            "name": "Abstract_Building_Purple",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Royal Purple and Silver color scheme. Abstract geometric shapes rising to form a skyscraper. Represents career elevation and executive search. Sophisticated, luxury feel. White background."
        },
        {
            "name": "Compass_Precision_Blue",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Slate Blue and Copper color scheme. A detailed drafting compass overlaid on a subtle grid background. Represents precision recruiting. Technical, engineering aesthetic. White background."
        },
        {
            "name": "Globe_Network_Multi",
            "prompt": "Generate an image: High-fidelity professional logo for 'LEMMIK CONSTRUCTION RECRUITING'. Navy Blue, Green, and Grey multicolor. A stylized globe constructed from interconnected nodes and beams. Represents a wide network of candidates. Global, connected feel. White background."
        }
    ]
    
    print("🍌 Creating 10 Detailed, Varied-Color Logos with Nano Banana Pro...")
    print("🎨 Colors: Navy, Orange, Teal, Red, Gold, Green, Yellow, Purple, Slate, Multi")
    print("=" * 70)
    
    model = genai.GenerativeModel('nano-banana-pro-preview')
    created_logos = []
    
    for i, concept in enumerate(logo_concepts, 1):
        print(f"\n🎨 Generating Logo {i}/10: {concept['name']}")
        print(f"   Prompt: {concept['prompt'][:80]}...")
        
        try:
            response = model.generate_content(
                concept['prompt'],
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
                            
                            filename = f"detailed_logo_{i:02d}_{concept['name']}.{ext}"
                            
                            with open(filename, 'wb') as f:
                                f.write(image_data)
                            
                            file_size = os.path.getsize(filename)
                            print(f"   ✅ SAVED: {filename}")
                            print(f"      📊 Size: {file_size/1024:.1f} KB")
                            
                            created_logos.append(filename)
                            break
                    else:
                        print(f"   ❌ No image data found")
                else:
                    print(f"   ❌ No content parts")
            else:
                print(f"   ❌ No candidates")
                
        except Exception as e:
            print(f"   ❌ Error creating {concept['name']}: {e}")
            continue
    
    print("\n" + "=" * 70)
    if created_logos:
        print(f"🎯 SUCCESS! Created {len(created_logos)} detailed logos!")
        print(f"\n📁 Generated Files:")
        for logo in created_logos:
            print(f"   - {logo}")
        print(f"\n🖼️  Find them at: \\\\wsl$\\Ubuntu\\home\\charl\\.openclaw\\workspace")
    else:
        print(f"❌ No logos were successfully created")

if __name__ == "__main__":
    create_detailed_logos()

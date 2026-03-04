#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv('.env.gmail')

def create_professional_logos():
    """Create 10 professional logos using Nano Banana Pro image generation"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    # Professional logo concepts based on Nano Banana Pro descriptions
    logo_concepts = [
        {
            "name": "Rising_Cityscape",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color scheme. Clean circular border frame with three vertical building bars of different heights inside representing modern city skyline. Simple geometric design on white background. Corporate Fortune 500 style logo."
        },
        {
            "name": "Keystone_Bridge", 
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border containing abstract stone bridge arch with central keystone connecting block. Clean geometric construction architecture theme. Simple design on white background. Corporate style."
        },
        {
            "name": "Industrial_Compass",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border with geometric compass/caliper engineering precision tool design. Construction engineering theme. Clean simple lines on white background. Fortune 500 corporate style."
        },
        {
            "name": "Growth_Arrow_Blocks",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border containing modular building blocks arranged ascending to form upward arrow. Growth and career progress theme. Simple geometric shapes on white background. Corporate design."
        },
        {
            "name": "Steel_I_Beam",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border with industrial steel I-beam cross-section shaped like letter 'L' for Lemmik. Heavy construction industrial strength theme. Simple strong design on white background."
        },
        {
            "name": "Blueprint_Grid",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border containing architectural blueprint planning grid with precise center target point. Technical planning theme. Clean geometric lines on white background. Corporate style."
        },
        {
            "name": "Bridge_Connection",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border with suspension bridge cable design connecting two points. Infrastructure and connection theme. Simple professional appearance on white background."
        },
        {
            "name": "Tower_Crane",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border containing abstract tower crane construction equipment silhouette. Building and construction power theme. Clean geometric design on white background."
        },
        {
            "name": "Team_Structure",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border with geometric human figure composed of architectural building blocks. People and construction team theme. Minimalist design on white background. Corporate style."
        },
        {
            "name": "Quality_Shield_Gear",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING' company. Forest green (#1E5128) color. Circular border containing industrial gear-shield hybrid shape with diamond precision center. Quality and reliability theme. Professional corporate appearance on white background."
        }
    ]
    
    print("🍌 Creating Professional Logos with Nano Banana Pro...")
    print("🌲 Forest Green Construction Recruiting Logos")
    print("=" * 65)
    
    model = genai.GenerativeModel('nano-banana-pro-preview')
    created_logos = []
    
    for i, concept in enumerate(logo_concepts, 1):
        print(f"\n🎨 Generating Logo {i}: {concept['name']}")
        print(f"   Theme: {concept['prompt'][60:120]}...")
        
        try:
            response = model.generate_content(
                concept['prompt'],
                generation_config=genai.types.GenerationConfig(
                    temperature=0.6,  # Slightly more consistent
                    top_p=0.8,
                    max_output_tokens=2048,
                )
            )
            
            # Extract image data
            if hasattr(response, 'candidates') and response.candidates:
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and candidate.content.parts:
                    for part in candidate.content.parts:
                        if hasattr(part, 'inline_data') and part.inline_data and part.inline_data.data:
                            # Found image data!
                            image_data = part.inline_data.data
                            mime_type = part.inline_data.mime_type
                            
                            # Determine file extension
                            ext = 'png'
                            if 'jpeg' in mime_type or 'jpg' in mime_type:
                                ext = 'jpg'
                            
                            filename = f"professional_logo_{i:02d}_{concept['name']}.{ext}"
                            
                            # Save image
                            with open(filename, 'wb') as f:
                                f.write(base64.b64decode(image_data))
                            
                            file_size = os.path.getsize(filename)
                            print(f"   ✅ SAVED: {filename}")
                            print(f"      Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
                            
                            created_logos.append(filename)
                            break
                    else:
                        print(f"   ❌ No image data found in response")
                else:
                    print(f"   ❌ No content parts in response")
            else:
                print(f"   ❌ No candidates in response")
                
        except Exception as e:
            print(f"   ❌ Error creating {concept['name']}: {e}")
            continue
    
    print("\n" + "=" * 65)
    if created_logos:
        print(f"🎯 SUCCESS! Created {len(created_logos)} professional logos!")
        print(f"🌲 All logos feature forest green (#1E5128) with corporate styling")
        print(f"💼 Professional Fortune 500-level design quality")
        
        print(f"\n📁 Generated Logo Files:")
        total_size = 0
        for logo in created_logos:
            size = os.path.getsize(logo)
            total_size += size
            print(f"   ✅ {logo} ({size/1024:.1f} KB)")
        
        print(f"\n📊 Total: {len(created_logos)} logos, {total_size/1024/1024:.1f} MB")
        print(f"\n🖼️  View in Windows Explorer: \\\\wsl$\\Ubuntu\\home\\charl\\.openclaw\\workspace")
        
    else:
        print(f"❌ No logos were successfully created")
    
    return created_logos

if __name__ == "__main__":
    logos = create_professional_logos()
    
    if logos:
        print(f"\n🏆 MISSION ACCOMPLISHED!")
        print(f"   Your professional construction recruiting logos are ready!")
        print(f"   Each logo is unique, professional, and industry-relevant.")
        print(f"   Perfect for business cards, website, and marketing materials.")
    else:
        print(f"\n💡 If logos didn't generate, try running again.")
        print(f"   Nano Banana Pro sometimes needs multiple attempts.")
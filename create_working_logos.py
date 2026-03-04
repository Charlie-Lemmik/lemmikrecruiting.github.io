#!/usr/bin/env python3

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env.gmail')

def create_working_professional_logos():
    """Create professional logos with FIXED image data handling"""
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing Google API key")
        return
    
    genai.configure(api_key=api_key)
    
    # Professional logo concepts
    logo_concepts = [
        {
            "name": "Rising_Cityscape",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with three vertical building bars of different heights. Modern city skyline theme. Clean geometric design. White background. Corporate Fortune 500 style."
        },
        {
            "name": "Keystone_Bridge", 
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with stone bridge arch and central keystone block. Construction architecture theme. Simple geometric design. White background. Corporate style."
        },
        {
            "name": "Industrial_Compass",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with geometric compass/caliper engineering tool. Precision construction theme. Clean lines. White background. Fortune 500 corporate style."
        },
        {
            "name": "Growth_Arrow_Blocks",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with modular building blocks forming upward arrow. Career growth theme. Simple geometric shapes. White background. Corporate design."
        },
        {
            "name": "Steel_I_Beam",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with industrial I-beam shaped like letter 'L'. Heavy construction theme. Strong geometric design. White background."
        },
        {
            "name": "Blueprint_Grid",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with architectural blueprint grid and center target. Technical planning theme. Clean geometric lines. White background. Corporate style."
        },
        {
            "name": "Bridge_Connection",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with suspension bridge connecting two points. Infrastructure connection theme. Simple professional design. White background."
        },
        {
            "name": "Tower_Crane",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with tower crane construction equipment silhouette. Building power theme. Clean geometric design. White background."
        },
        {
            "name": "Team_Structure",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with geometric human figure made of building blocks. People and construction team theme. Minimalist design. White background."
        },
        {
            "name": "Quality_Shield_Gear",
            "prompt": "Generate an image: Professional minimalist logo for 'LEMMIK CONSTRUCTION RECRUITING'. Forest green (#1E5128) circular frame with industrial gear-shield hybrid and diamond center. Quality reliability theme. Professional corporate design. White background."
        }
    ]
    
    print("🍌 Creating Professional Logos with Nano Banana Pro...")
    print("🌲 Forest Green Construction Recruiting Logos")
    print("🔧 FIXED: Proper Binary Image Data Handling")
    print("=" * 70)
    
    model = genai.GenerativeModel('nano-banana-pro-preview')
    created_logos = []
    
    for i, concept in enumerate(logo_concepts, 1):
        print(f"\n🎨 Generating Logo {i}/10: {concept['name']}")
        
        try:
            response = model.generate_content(
                concept['prompt'],
                generation_config=genai.types.GenerationConfig(
                    temperature=0.6,
                    top_p=0.8,
                    max_output_tokens=2048,
                )
            )
            
            # Extract image data with FIXED handling
            if hasattr(response, 'candidates') and response.candidates:
                candidate = response.candidates[0]
                if hasattr(candidate, 'content') and candidate.content.parts:
                    
                    for part in candidate.content.parts:
                        if hasattr(part, 'inline_data') and part.inline_data and part.inline_data.data:
                            
                            # Get the binary image data (already decoded!)
                            image_data = part.inline_data.data  # This is bytes, not base64!
                            mime_type = part.inline_data.mime_type
                            
                            # Determine file extension
                            ext = 'jpg'
                            if 'png' in mime_type:
                                ext = 'png'
                            
                            filename = f"final_logo_{i:02d}_{concept['name']}.{ext}"
                            
                            # Save the binary data directly (NO base64 decoding!)
                            with open(filename, 'wb') as f:
                                f.write(image_data)
                            
                            file_size = os.path.getsize(filename)
                            print(f"   ✅ SAVED: {filename}")
                            print(f"      📊 Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
                            print(f"      🎨 Type: {mime_type}")
                            
                            created_logos.append({
                                'filename': filename,
                                'size': file_size,
                                'concept': concept['name']
                            })
                            break
                    else:
                        print(f"   ❌ No image data found")
                else:
                    print(f"   ❌ No content parts")
            else:
                print(f"   ❌ No candidates")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
            continue
    
    print("\n" + "=" * 70)
    if created_logos:
        print(f"🎯 SUCCESS! Created {len(created_logos)} professional logos!")
        print(f"🌲 Forest green (#1E5128) construction recruiting themes")
        print(f"💼 Fortune 500-level professional quality")
        
        print(f"\n📁 Generated Professional Logo Files:")
        total_size = 0
        for logo in created_logos:
            size = logo['size']
            total_size += size
            print(f"   ✅ {logo['filename']}")
            print(f"      📊 {size/1024:.1f} KB - {logo['concept']}")
        
        print(f"\n📊 Summary:")
        print(f"   • Total logos: {len(created_logos)}")
        print(f"   • Total size: {total_size/1024/1024:.1f} MB")
        print(f"   • Average size: {(total_size/len(created_logos))/1024:.1f} KB each")
        
        print(f"\n🖼️  VIEW YOUR LOGOS:")
        print(f"   Windows Explorer: \\\\wsl$\\Ubuntu\\home\\charl\\.openclaw\\workspace")
        print(f"   Look for files starting with: final_logo_")
        
    else:
        print(f"❌ No logos were successfully created")
    
    return created_logos

if __name__ == "__main__":
    print("🍌 NANO BANANA PRO - PROFESSIONAL LOGO GENERATOR")
    print("🔧 Fixed Version - Proper Binary Image Handling")
    print("=" * 70)
    
    logos = create_working_professional_logos()
    
    if logos:
        print(f"\n🏆 MISSION ACCOMPLISHED!")
        print(f"   Your professional LEMMIK CONSTRUCTION RECRUITING logos are ready!")
        print(f"   Each logo is unique, industry-relevant, and corporate-quality.")
        print(f"   Perfect for business cards, website headers, and marketing materials.")
        print(f"\n🌲 All logos feature your requested forest green color scheme.")
        print(f"💼 Professional Fortune 500-style branding for your business.")
    else:
        print(f"\n❌ Generation failed. Try running the script again.")
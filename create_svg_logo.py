#!/usr/bin/env python3
import svgwrite

def create_lemmik_logo():
    """Create a professional SVG logo for Lemmik Construction Recruiting"""
    # Colors matching the new website theme
    NAVY = '#0a192f'  # Deep Navy
    GOLD = '#fbbf24'  # Construction Gold/Amber
    GREY = '#64748b'  # Slate Grey
    
    # Create Drawing
    dwg = svgwrite.Drawing('lemmik_logo_professional.svg', size=('400px', '100px'), profile='full')
    
    # Group for text styles
    # Using system fonts that look professional (Impact/Helvetica/Arial)
    
    # 1. The Icon (Abstract L-Beam / Building Block)
    # Vertical pillar (Navy)
    dwg.add(dwg.rect(insert=(10, 10), size=(15, 65), rx=2, ry=2, fill=NAVY))
    # Horizontal foundation (Gold)
    dwg.add(dwg.rect(insert=(10, 65), size=(45, 10), rx=2, ry=2, fill=GOLD))
    # Small accent block (top right of L)
    dwg.add(dwg.rect(insert=(30, 10), size=(15, 15), rx=2, ry=2, fill=GREY))

    # 2. Main Text "LEMMIK"
    # We use a bold, heavy sans-serif font
    text_group = dwg.g(font_family="Arial, Helvetica, sans-serif", font_weight="bold")
    
    # "LEMMIK" in Navy
    text_group.add(dwg.text("LEMMIK", insert=(65, 75), font_size="60px", fill=NAVY, letter_spacing="-2px"))
    
    # 3. Subtext "RECRUITING"
    # Spaced out, smaller, in Grey
    text_group.add(dwg.text("RECRUITING", insert=(68, 92), font_size="14px", fill=GREY, letter_spacing="6px", font_weight="normal"))
    
    dwg.add(text_group)
    
    dwg.save()
    print("✅ Created: lemmik_logo_professional.svg")

if __name__ == '__main__':
    create_lemmik_logo()

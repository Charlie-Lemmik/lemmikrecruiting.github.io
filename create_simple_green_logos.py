#!/usr/bin/env python3

import svgwrite
from svgwrite import cm, mm
import math

def create_logo_1_vertical_bars():
    """Logo 1: Vertical bars in circle (like the reference)"""
    
    dwg = svgwrite.Drawing('lemmik_logo_1_vertical_bars.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Vertical bars (varying heights for building silhouette)
    bars = [
        (120, 180, 8, 40),   # Short
        (135, 160, 8, 60),   # Medium
        (150, 140, 8, 80),   # Tall
        (165, 170, 8, 50),   # Medium-short
        (180, 155, 8, 65)    # Medium-tall
    ]
    
    for x, y, width, height in bars:
        dwg.add(dwg.rect(insert=(x, y), size=(width, height), fill=forest_green))
    
    dwg.save()
    return 'lemmik_logo_1_vertical_bars.svg'

def create_logo_2_construction_tools():
    """Logo 2: Simple construction tools in circle"""
    
    dwg = svgwrite.Drawing('lemmik_logo_2_construction_tools.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Simple hammer shape
    dwg.add(dwg.rect(insert=(140, 120), size=(20, 60), fill=forest_green))  # Handle
    dwg.add(dwg.rect(insert=(130, 110), size=(40, 20), fill=forest_green))  # Head
    
    # Simple wrench
    dwg.add(dwg.rect(insert=(160, 160), size=(8, 40), fill=forest_green))   # Handle
    dwg.add(dwg.circle(center=(164, 155), r=8, 
                      fill='none', stroke=forest_green, stroke_width=4))    # Head
    
    dwg.save()
    return 'lemmik_logo_2_construction_tools.svg'

def create_logo_3_hexagon_pattern():
    """Logo 3: Hexagonal pattern (industrial/construction)"""
    
    dwg = svgwrite.Drawing('lemmik_logo_3_hexagon_pattern.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Central hexagon
    hex_points = []
    for i in range(6):
        angle = i * 60 * math.pi / 180
        x = 150 + 30 * math.cos(angle)
        y = 150 + 30 * math.sin(angle)
        hex_points.append((x, y))
    
    dwg.add(dwg.polygon(points=hex_points, fill=forest_green))
    
    # Smaller surrounding hexagons
    for i in range(6):
        angle = i * 60 * math.pi / 180
        center_x = 150 + 50 * math.cos(angle)
        center_y = 150 + 50 * math.sin(angle)
        
        small_hex = []
        for j in range(6):
            hex_angle = j * 60 * math.pi / 180
            x = center_x + 15 * math.cos(hex_angle)
            y = center_y + 15 * math.sin(hex_angle)
            small_hex.append((x, y))
        
        dwg.add(dwg.polygon(points=small_hex, fill=forest_green, opacity=0.6))
    
    dwg.save()
    return 'lemmik_logo_3_hexagon_pattern.svg'

def create_logo_4_l_beam():
    """Logo 4: Simple L-beam in circle"""
    
    dwg = svgwrite.Drawing('lemmik_logo_4_l_beam.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # L-beam shape
    dwg.add(dwg.rect(insert=(120, 110), size=(15, 80), fill=forest_green))  # Vertical
    dwg.add(dwg.rect(insert=(120, 175), size=(60, 15), fill=forest_green))  # Horizontal
    
    dwg.save()
    return 'lemmik_logo_4_l_beam.svg'

def create_logo_5_crane():
    """Logo 5: Simple crane silhouette"""
    
    dwg = svgwrite.Drawing('lemmik_logo_5_crane.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Crane mast
    dwg.add(dwg.rect(insert=(145, 110), size=(10, 80), fill=forest_green))
    
    # Crane jib (horizontal arm)
    dwg.add(dwg.rect(insert=(155, 115), size=(40, 8), fill=forest_green))
    
    # Counter-jib
    dwg.add(dwg.rect(insert=(125, 115), size=(20, 8), fill=forest_green))
    
    # Hook line
    dwg.add(dwg.line(start=(190, 123), end=(190, 160), 
                    stroke=forest_green, stroke_width=2))
    
    dwg.save()
    return 'lemmik_logo_5_crane.svg'

def create_logo_6_gear():
    """Logo 6: Simple gear/cog shape"""
    
    dwg = svgwrite.Drawing('lemmik_logo_6_gear.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Gear outer circle
    dwg.add(dwg.circle(center=(150, 150), r=40, 
                      fill='none', stroke=forest_green, stroke_width=6))
    
    # Gear teeth (simplified as rectangles)
    for i in range(8):
        angle = i * 45 * math.pi / 180
        x = 150 + 45 * math.cos(angle) - 4
        y = 150 + 45 * math.sin(angle) - 8
        
        tooth = dwg.rect(insert=(x, y), size=(8, 16), fill=forest_green)
        tooth.attribs['transform'] = f'rotate({i*45} {x+4} {y+8})'
        dwg.add(tooth)
    
    # Center circle
    dwg.add(dwg.circle(center=(150, 150), r=15, fill=forest_green))
    
    dwg.save()
    return 'lemmik_logo_6_gear.svg'

def create_logo_7_blueprint():
    """Logo 7: Blueprint/architectural lines"""
    
    dwg = svgwrite.Drawing('lemmik_logo_7_blueprint.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Blueprint-style building outline
    building = [
        (120, 180), (120, 140), (140, 130), (160, 130),
        (180, 140), (180, 180), (120, 180)
    ]
    dwg.add(dwg.polyline(points=building, fill='none', 
                        stroke=forest_green, stroke_width=4))
    
    # Internal structural lines
    dwg.add(dwg.line(start=(140, 130), end=(140, 180), 
                    stroke=forest_green, stroke_width=2))
    dwg.add(dwg.line(start=(160, 130), end=(160, 180), 
                    stroke=forest_green, stroke_width=2))
    dwg.add(dwg.line(start=(120, 160), end=(180, 160), 
                    stroke=forest_green, stroke_width=2))
    
    dwg.save()
    return 'lemmik_logo_7_blueprint.svg'

def create_logo_8_triangle():
    """Logo 8: Simple triangle/pyramid (stability)"""
    
    dwg = svgwrite.Drawing('lemmik_logo_8_triangle.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Large triangle
    triangle = [(150, 120), (120, 180), (180, 180)]
    dwg.add(dwg.polygon(points=triangle, fill=forest_green))
    
    # Smaller internal triangles for detail
    small_tri1 = [(150, 135), (135, 165), (165, 165)]
    dwg.add(dwg.polygon(points=small_tri1, fill='white'))
    
    dwg.save()
    return 'lemmik_logo_8_triangle.svg'

def create_logo_9_bridge():
    """Logo 9: Simple bridge silhouette"""
    
    dwg = svgwrite.Drawing('lemmik_logo_9_bridge.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Bridge deck
    dwg.add(dwg.rect(insert=(110, 160), size=(80, 8), fill=forest_green))
    
    # Bridge towers
    dwg.add(dwg.rect(insert=(125, 130), size=(8, 40), fill=forest_green))
    dwg.add(dwg.rect(insert=(167, 130), size=(8, 40), fill=forest_green))
    
    # Cables (simplified)
    dwg.add(dwg.line(start=(129, 130), end=(150, 160), 
                    stroke=forest_green, stroke_width=2))
    dwg.add(dwg.line(start=(129, 130), end=(110, 160), 
                    stroke=forest_green, stroke_width=2))
    dwg.add(dwg.line(start=(171, 130), end=(150, 160), 
                    stroke=forest_green, stroke_width=2))
    dwg.add(dwg.line(start=(171, 130), end=(190, 160), 
                    stroke=forest_green, stroke_width=2))
    
    dwg.save()
    return 'lemmik_logo_9_bridge.svg'

def create_logo_10_diamond():
    """Logo 10: Diamond/precision symbol"""
    
    dwg = svgwrite.Drawing('lemmik_logo_10_diamond.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Outer circle
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Diamond shape
    diamond = [(150, 120), (180, 150), (150, 180), (120, 150)]
    dwg.add(dwg.polygon(points=diamond, fill=forest_green))
    
    # Inner diamond detail
    inner_diamond = [(150, 135), (165, 150), (150, 165), (135, 150)]
    dwg.add(dwg.polygon(points=inner_diamond, fill='white'))
    
    # Center dot
    dwg.add(dwg.circle(center=(150, 150), r=5, fill=forest_green))
    
    dwg.save()
    return 'lemmik_logo_10_diamond.svg'

def create_all_simple_logos():
    """Create all 10 simple, clean logos"""
    
    print("🌲 Creating 10 Simple Forest Green Logos...")
    print("Inspired by clean, geometric design aesthetic")
    print("=" * 60)
    
    logos = [
        create_logo_1_vertical_bars(),
        create_logo_2_construction_tools(),
        create_logo_3_hexagon_pattern(),
        create_logo_4_l_beam(),
        create_logo_5_crane(),
        create_logo_6_gear(),
        create_logo_7_blueprint(),
        create_logo_8_triangle(),
        create_logo_9_bridge(),
        create_logo_10_diamond()
    ]
    
    for i, logo in enumerate(logos, 1):
        print(f"✅ Created Logo {i}: {logo}")
    
    print("=" * 60)
    print("🎯 All 10 forest green logos created!")
    print("\n🌲 Design Features:")
    print("   - Forest green color (#1E5128)")
    print("   - Clean, geometric shapes")
    print("   - Construction industry themes")
    print("   - Circular framing (consistent branding)")
    print("   - Minimalist, professional aesthetic")
    
    print("\n📁 Files saved as SVG:")
    for i in range(1, 11):
        print(f"   - lemmik_logo_{i}_*.svg")

if __name__ == "__main__":
    create_all_simple_logos()
#!/usr/bin/env python3

import svgwrite
from svgwrite import cm, mm
import math

def create_logo_1_rising_cityscape():
    """Concept 1: The Rising Cityscape - 3 vertical bars of different heights"""
    
    dwg = svgwrite.Drawing('nano_logo_1_rising_cityscape.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Medium-thick circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=6))
    
    # Horizontal baseline at lower third
    baseline_y = 150 + (100 / 3)  # Lower third of circle
    
    # Three vertical bars rising from baseline
    bar_width = 20
    bar_spacing = 25
    
    # Left bar (2/3 height of center)
    left_height = 60
    dwg.add(dwg.rect(insert=(120, baseline_y - left_height), 
                    size=(bar_width, left_height), fill=forest_green))
    
    # Center bar (tallest, nearly touching top)
    center_height = 90
    dwg.add(dwg.rect(insert=(145, baseline_y - center_height), 
                    size=(bar_width, center_height), fill=forest_green))
    
    # Right bar (1/2 height of center)
    right_height = 45
    dwg.add(dwg.rect(insert=(170, baseline_y - right_height), 
                    size=(bar_width, right_height), fill=forest_green))
    
    dwg.save()
    return 'nano_logo_1_rising_cityscape.svg'

def create_logo_2_keystone_link():
    """Concept 2: The Keystone Link - Archway with keystone block"""
    
    dwg = svgwrite.Drawing('nano_logo_2_keystone_link.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=6))
    
    # Left arch shape (thick outline)
    left_arch = dwg.path(d="M 100 200 Q 100 120 150 120", 
                        fill='none', stroke=forest_green, stroke_width=8)
    dwg.add(left_arch)
    
    # Right arch shape (mirror image)
    right_arch = dwg.path(d="M 200 200 Q 200 120 150 120", 
                         fill='none', stroke=forest_green, stroke_width=8)
    dwg.add(right_arch)
    
    # Keystone square at apex
    dwg.add(dwg.rect(insert=(135, 105), size=(30, 30), fill=forest_green))
    
    dwg.save()
    return 'nano_logo_2_keystone_link.svg'

def create_logo_3_geometric_compass():
    """Concept 3: The Geometric Compass - Abstract compass/caliper"""
    
    dwg = svgwrite.Drawing('nano_logo_3_geometric_compass.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Thin circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=3))
    
    # Two elongated triangles forming compass legs
    left_triangle = [(150, 100), (120, 180), (135, 180)]
    right_triangle = [(150, 100), (180, 180), (165, 180)]
    
    dwg.add(dwg.polygon(points=left_triangle, fill='none', 
                       stroke=forest_green, stroke_width=3))
    dwg.add(dwg.polygon(points=right_triangle, fill='none', 
                       stroke=forest_green, stroke_width=3))
    
    # Small circle between triangle tips
    dwg.add(dwg.circle(center=(150, 180), r=8, 
                      fill='none', stroke=forest_green, stroke_width=3))
    
    # Horizontal arc for measurement
    arc = dwg.path(d="M 120 170 Q 150 160 180 170", 
                  fill='none', stroke=forest_green, stroke_width=3)
    dwg.add(arc)
    
    dwg.save()
    return 'nano_logo_3_geometric_compass.svg'

def create_logo_4_modular_arrow():
    """Concept 4: The Modular Arrow - Building blocks forming upward path"""
    
    dwg = svgwrite.Drawing('nano_logo_4_modular_arrow.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=6))
    
    # Three squares stepping upward diagonally
    square_size = 25
    
    # Bottom left square
    dwg.add(dwg.rect(insert=(105, 175), size=(square_size, square_size), 
                    fill=forest_green))
    
    # Middle square
    dwg.add(dwg.rect(insert=(125, 155), size=(square_size, square_size), 
                    fill=forest_green))
    
    # Top square
    dwg.add(dwg.rect(insert=(145, 135), size=(square_size, square_size), 
                    fill=forest_green))
    
    # Triangle arrow tip
    triangle_points = [(170, 135), (185, 147.5), (170, 160)]
    dwg.add(dwg.polygon(points=triangle_points, fill=forest_green))
    
    dwg.save()
    return 'nano_logo_4_modular_arrow.svg'

def create_logo_5_i_beam_monogram():
    """Concept 5: The I-Beam Monogram - Industrial "L" from I-beam"""
    
    dwg = svgwrite.Drawing('nano_logo_5_i_beam_monogram.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Thick circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # I-beam "L" - vertical part
    dwg.add(dwg.rect(insert=(120, 100), size=(25, 80), fill=forest_green))
    
    # I-beam "L" - horizontal part (base)
    dwg.add(dwg.rect(insert=(120, 155), size=(60, 25), fill=forest_green))
    
    dwg.save()
    return 'nano_logo_5_i_beam_monogram.svg'

def create_logo_6_blueprint_grid():
    """Concept 6: The Blueprint Grid - 3x3 grid with center circle"""
    
    dwg = svgwrite.Drawing('nano_logo_6_blueprint_grid.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Thin circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=3))
    
    # Incomplete 3x3 grid - only center lines and center square
    grid_start = 100
    grid_end = 200
    
    # Central vertical line
    dwg.add(dwg.line(start=(150, grid_start), end=(150, grid_end), 
                    stroke=forest_green, stroke_width=2))
    
    # Central horizontal line
    dwg.add(dwg.line(start=(grid_start, 150), end=(grid_end, 150), 
                    stroke=forest_green, stroke_width=2))
    
    # Center square lines
    center_size = 33
    center_start = 150 - center_size//2
    center_end = 150 + center_size//2
    
    # Top line of center square
    dwg.add(dwg.line(start=(center_start, center_start), 
                    end=(center_end, center_start), 
                    stroke=forest_green, stroke_width=2))
    
    # Bottom line of center square
    dwg.add(dwg.line(start=(center_start, center_end), 
                    end=(center_end, center_end), 
                    stroke=forest_green, stroke_width=2))
    
    # Left line of center square
    dwg.add(dwg.line(start=(center_start, center_start), 
                    end=(center_start, center_end), 
                    stroke=forest_green, stroke_width=2))
    
    # Right line of center square
    dwg.add(dwg.line(start=(center_end, center_start), 
                    end=(center_end, center_end), 
                    stroke=forest_green, stroke_width=2))
    
    # Solid circle in center
    dwg.add(dwg.circle(center=(150, 150), r=12, fill=forest_green))
    
    dwg.save()
    return 'nano_logo_6_blueprint_grid.svg'

def create_logo_7_bridge_span():
    """Concept 7: The Bridge Span - Suspension bridge"""
    
    dwg = svgwrite.Drawing('nano_logo_7_bridge_span.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=6))
    
    # Two vertical pillars
    dwg.add(dwg.rect(insert=(80, 110), size=(12, 60), fill=forest_green))
    dwg.add(dwg.rect(insert=(208, 110), size=(12, 60), fill=forest_green))
    
    # Main cable arc
    cable = dwg.path(d="M 86 110 Q 150 90 214 110", 
                    fill='none', stroke=forest_green, stroke_width=6)
    dwg.add(cable)
    
    # Road deck (horizontal line)
    dwg.add(dwg.line(start=(86, 160), end=(214, 160), 
                    stroke=forest_green, stroke_width=6))
    
    dwg.save()
    return 'nano_logo_7_bridge_span.svg'

def create_logo_8_ascending_crane():
    """Concept 8: The Ascending Crane - Abstract crane with hook"""
    
    dwg = svgwrite.Drawing('nano_logo_8_ascending_crane.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=6))
    
    # Vertical mast on left
    dwg.add(dwg.line(start=(110, 80), end=(110, 200), 
                    stroke=forest_green, stroke_width=8))
    
    # Diagonal jib extending upward to right
    dwg.add(dwg.line(start=(110, 80), end=(180, 60), 
                    stroke=forest_green, stroke_width=8))
    
    # Vertical hook line
    dwg.add(dwg.line(start=(180, 60), end=(180, 140), 
                    stroke=forest_green, stroke_width=4))
    
    # Load block (small square)
    dwg.add(dwg.rect(insert=(175, 140), size=(10, 10), fill=forest_green))
    
    dwg.save()
    return 'nano_logo_8_ascending_crane.svg'

def create_logo_9_human_structure():
    """Concept 9: The Human Structure - Person from geometric shapes"""
    
    dwg = svgwrite.Drawing('nano_logo_9_human_structure.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=6))
    
    # Head (solid circle)
    dwg.add(dwg.circle(center=(150, 110), r=18, fill=forest_green))
    
    # Torso (trapezoid - wider at bottom)
    torso_points = [(135, 135), (165, 135), (170, 170), (130, 170)]
    dwg.add(dwg.polygon(points=torso_points, fill=forest_green))
    
    # Base (solid rectangle)
    dwg.add(dwg.rect(insert=(125, 175), size=(50, 20), fill=forest_green))
    
    dwg.save()
    return 'nano_logo_9_human_structure.svg'

def create_logo_10_gear_shield():
    """Concept 10: The Gear Shield - Shield-shaped gear with diamond"""
    
    dwg = svgwrite.Drawing('nano_logo_10_gear_shield.svg', 
                          size=('300px', '300px'),
                          viewBox='0 0 300 300')
    
    forest_green = '#1E5128'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Thick circular frame
    dwg.add(dwg.circle(center=(150, 150), r=100, 
                      fill='none', stroke=forest_green, stroke_width=8))
    
    # Shield-like gear shape (elongated vertically)
    shield_path = dwg.path(d="M 150 90 C 180 90 190 120 190 150 C 190 180 180 210 150 210 C 120 210 110 180 110 150 C 110 120 120 90 150 90 Z",
                          fill=forest_green)
    dwg.add(shield_path)
    
    # Six square teeth protruding
    tooth_size = 8
    positions = [
        (146, 82),   # Top
        (170, 105),  # Top right
        (170, 175),  # Bottom right
        (146, 210),  # Bottom
        (130, 175),  # Bottom left
        (130, 105)   # Top left
    ]
    
    for x, y in positions:
        dwg.add(dwg.rect(insert=(x, y), size=(tooth_size, tooth_size), 
                        fill=forest_green))
    
    # Central diamond (negative space - white)
    diamond_points = [(150, 130), (165, 150), (150, 170), (135, 150)]
    dwg.add(dwg.polygon(points=diamond_points, fill='white'))
    
    dwg.save()
    return 'nano_logo_10_gear_shield.svg'

def create_all_nano_banana_logos():
    """Create all 10 logos based on Nano Banana Pro descriptions"""
    
    print("🍌 Creating Visual Logos from Nano Banana Pro Concepts...")
    print("🌲 Forest Green (#1E5128) - Professional Implementation")
    print("=" * 70)
    
    logos = [
        create_logo_1_rising_cityscape(),
        create_logo_2_keystone_link(),
        create_logo_3_geometric_compass(),
        create_logo_4_modular_arrow(),
        create_logo_5_i_beam_monogram(),
        create_logo_6_blueprint_grid(),
        create_logo_7_bridge_span(),
        create_logo_8_ascending_crane(),
        create_logo_9_human_structure(),
        create_logo_10_gear_shield()
    ]
    
    concept_names = [
        "The Rising Cityscape",
        "The Keystone Link", 
        "The Geometric Compass",
        "The Modular Arrow",
        "The I-Beam Monogram",
        "The Blueprint Grid",
        "The Bridge Span",
        "The Ascending Crane",
        "The Human Structure",
        "The Gear Shield"
    ]
    
    for i, (logo, name) in enumerate(zip(logos, concept_names), 1):
        print(f"✅ Created Logo {i}: {name}")
        print(f"   File: {logo}")
    
    print("=" * 70)
    print("🎯 All 10 Nano Banana Pro logos implemented!")
    print("\n🌲 Each logo features:")
    print("   - Forest green color (#1E5128)")  
    print("   - Professional circular framing")
    print("   - Sophisticated geometric design")
    print("   - Construction industry relevance")
    print("   - Fortune 500-level aesthetic")

if __name__ == "__main__":
    create_all_nano_banana_logos()
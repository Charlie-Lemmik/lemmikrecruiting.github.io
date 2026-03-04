#!/usr/bin/env python3

import svgwrite
from svgwrite import cm, mm
import math

def create_concept_1_structural_network():
    """Create Concept 1: The Structural Network - L-beam with neural network"""
    
    dwg = svgwrite.Drawing('lemmik_concept_1_structural_network.svg', 
                          size=('800px', '400px'),
                          viewBox='0 0 800 400')
    
    # Colors
    slate_blue = '#212F3D'
    electric_cyan = '#00D2E6'
    cool_gray = '#7F8C8D'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # L-beam structure (main beam)
    l_beam = dwg.g(id='l_beam')
    
    # Vertical part of L
    l_beam.add(dwg.rect(insert=(50, 100), size=(30, 180), 
                       fill=slate_blue, stroke='none'))
    
    # Horizontal part of L  
    l_beam.add(dwg.rect(insert=(50, 250), size=(120, 30), 
                       fill=slate_blue, stroke='none'))
    
    # Neural network nodes
    nodes = [
        (65, 130), (65, 170), (65, 210), (65, 240),
        (90, 265), (130, 265), (155, 265)
    ]
    
    # Add glowing nodes
    for i, (x, y) in enumerate(nodes):
        # Outer glow
        dwg.add(dwg.circle(center=(x, y), r=8, 
                          fill=electric_cyan, opacity=0.3))
        # Inner bright node
        dwg.add(dwg.circle(center=(x, y), r=4, 
                          fill=electric_cyan))
    
    # Connection lines between nodes
    connections = [
        ((65, 130), (65, 170)),
        ((65, 170), (65, 210)),
        ((65, 210), (65, 240)),
        ((65, 240), (90, 265)),
        ((90, 265), (130, 265)),
        ((130, 265), (155, 265))
    ]
    
    for start, end in connections:
        dwg.add(dwg.line(start=start, end=end, 
                        stroke=electric_cyan, stroke_width=2, opacity=0.7))
    
    dwg.add(l_beam)
    
    # Typography
    # LEMMIK
    dwg.add(dwg.text('LEMMIK', 
                    insert=(220, 220),
                    font_family='Montserrat, Arial Black, sans-serif',
                    font_size='48px',
                    font_weight='900',
                    fill=slate_blue))
    
    # CONSTRUCTION RECRUITING
    dwg.add(dwg.text('CONSTRUCTION RECRUITING', 
                    insert=(220, 250),
                    font_family='Open Sans, Arial, sans-serif',
                    font_size='16px',
                    font_weight='300',
                    fill=cool_gray,
                    letter_spacing='2px'))
    
    # Tagline
    dwg.add(dwg.text('Building Teams. Building Futures.', 
                    insert=(220, 280),
                    font_family='Open Sans, Arial, sans-serif',
                    font_size='14px',
                    font_style='italic',
                    fill=cool_gray))
    
    dwg.save()
    return 'lemmik_concept_1_structural_network.svg'

def create_concept_2_apex_keystone():
    """Create Concept 2: The Apex Keystone - Bridge keystone with circuit patterns"""
    
    dwg = svgwrite.Drawing('lemmik_concept_2_apex_keystone.svg', 
                          size=('800px', '500px'),
                          viewBox='0 0 800 500')
    
    # Colors  
    charcoal = '#36454F'
    copper = '#B87333'
    off_white = '#F4F6F7'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill=off_white))
    
    # Arch structure
    arch = dwg.g(id='arch')
    
    # Left pillar
    arch.add(dwg.rect(insert=(100, 150), size=(40, 150), 
                     fill=charcoal, stroke='none'))
    
    # Right pillar  
    arch.add(dwg.rect(insert=(260, 150), size=(40, 150), 
                     fill=charcoal, stroke='none'))
    
    # Arch stones (trapezoids)
    arch_stones = [
        [(140, 150), (170, 140), (170, 170), (140, 160)],  # Left stone
        [(170, 140), (200, 135), (200, 165), (170, 170)],  # Left-center
        [(200, 135), (230, 140), (230, 170), (200, 165)],  # Right-center  
        [(230, 140), (260, 150), (260, 160), (230, 170)]   # Right stone
    ]
    
    for stone in arch_stones:
        arch.add(dwg.polygon(points=stone, fill=charcoal, stroke='none'))
    
    # KEYSTONE (the central, special piece)
    keystone_points = [(185, 130), (215, 130), (220, 140), (210, 160), 
                      (190, 160), (180, 140)]
    arch.add(dwg.polygon(points=keystone_points, fill=copper, stroke='none'))
    
    # Circuit pattern on keystone (simple lines)
    circuit = dwg.g(id='circuit', opacity=0.6)
    circuit.add(dwg.line(start=(190, 140), end=(210, 140), 
                        stroke=off_white, stroke_width=1))
    circuit.add(dwg.line(start=(190, 150), end=(210, 150), 
                        stroke=off_white, stroke_width=1))
    circuit.add(dwg.circle(center=(200, 145), r=2, 
                          fill=off_white, stroke='none'))
    
    dwg.add(arch)
    dwg.add(circuit)
    
    # Typography (centered layout)
    # LEMMIK
    dwg.add(dwg.text('LEMMIK', 
                    insert=(200, 350),
                    font_family='Cinzel, Times, serif',
                    font_size='52px',
                    font_weight='bold',
                    fill=charcoal,
                    text_anchor='middle'))
    
    # CONSTRUCTION RECRUITING
    dwg.add(dwg.text('CONSTRUCTION RECRUITING', 
                    insert=(200, 385),
                    font_family='Gotham, Arial, sans-serif',
                    font_size='18px',
                    font_weight='500',
                    fill=charcoal,
                    text_anchor='middle',
                    letter_spacing='3px'))
    
    # Tagline
    dwg.add(dwg.text('Excellence in Executive Placement', 
                    insert=(200, 415),
                    font_family='Gotham, Arial, sans-serif',
                    font_size='14px',
                    font_style='italic',
                    fill=copper,
                    text_anchor='middle'))
    
    dwg.save()
    return 'lemmik_concept_2_apex_keystone.svg'

def create_concept_3_ascending_blueprint():
    """Create Concept 3: The Ascending Blueprint - Dynamic upward arrow"""
    
    dwg = svgwrite.Drawing('lemmik_concept_3_ascending_blueprint.svg', 
                          size=('800px', '400px'),
                          viewBox='0 0 800 400')
    
    # Colors
    forest_green = '#1E5128'  
    mint_lime = '#50C878'
    dark_graphite = '#2C3E50'
    
    # Background
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))
    
    # Blueprint grid pattern (subtle)
    grid = dwg.g(id='grid', opacity=0.1)
    for i in range(0, 200, 20):
        grid.add(dwg.line(start=(50+i, 100), end=(50+i, 280), 
                         stroke=dark_graphite, stroke_width=0.5))
        grid.add(dwg.line(start=(50, 100+i), end=(200, 100+i), 
                         stroke=dark_graphite, stroke_width=0.5))
    dwg.add(grid)
    
    # Ascending arrow layers
    arrow = dwg.g(id='ascending_arrow')
    
    # Layer 1 (bottom, widest)
    layer1_points = [(80, 260), (120, 260), (130, 240), (70, 240)]
    arrow.add(dwg.polygon(points=layer1_points, fill=forest_green, opacity=0.8))
    
    # Layer 2 (middle)  
    layer2_points = [(85, 240), (115, 240), (125, 220), (75, 220)]
    arrow.add(dwg.polygon(points=layer2_points, fill=forest_green, opacity=0.9))
    
    # Layer 3 (upper)
    layer3_points = [(90, 220), (110, 220), (120, 200), (80, 200)]
    arrow.add(dwg.polygon(points=layer3_points, fill=forest_green))
    
    # Arrow tip (precise point)
    tip_points = [(95, 200), (105, 200), (100, 180)]
    arrow.add(dwg.polygon(points=tip_points, fill=mint_lime))
    
    # Glowing effect on tip
    dwg.add(dwg.circle(center=(100, 185), r=8, 
                      fill=mint_lime, opacity=0.3))
    dwg.add(dwg.circle(center=(100, 185), r=3, 
                      fill=mint_lime))
    
    dwg.add(arrow)
    
    # Typography
    # LEMMIK
    dwg.add(dwg.text('LEMMIK', 
                    insert=(250, 220),
                    font_family='Futura, Avant Garde Gothic, Arial, sans-serif',
                    font_size='48px',
                    font_weight='bold',
                    fill=forest_green))
    
    # CONSTRUCTION RECRUITING
    dwg.add(dwg.text('CONSTRUCTION RECRUITING', 
                    insert=(250, 250),
                    font_family='Futura, Arial, sans-serif',
                    font_size='16px',
                    font_weight='300',
                    fill=dark_graphite,
                    letter_spacing='2px'))
    
    # Tagline
    dwg.add(dwg.text('Smart Recruiting. Strong Results.', 
                    insert=(250, 280),
                    font_family='Futura, Arial, sans-serif',
                    font_size='14px',
                    font_style='italic',
                    fill=mint_lime))
    
    dwg.save()
    return 'lemmik_concept_3_ascending_blueprint.svg'

def create_all_professional_logos():
    """Create all three professional logo concepts"""
    
    print("🎨 Creating Professional Lemmik Logo Concepts...")
    print("Based on Nano Banana Pro AI design concepts")
    print("=" * 60)
    
    # Create all three concepts
    concept1 = create_concept_1_structural_network()
    print(f"✅ Created Concept 1: The Structural Network")
    print(f"   File: {concept1}")
    
    concept2 = create_concept_2_apex_keystone()  
    print(f"✅ Created Concept 2: The Apex Keystone")
    print(f"   File: {concept2}")
    
    concept3 = create_concept_3_ascending_blueprint()
    print(f"✅ Created Concept 3: The Ascending Blueprint") 
    print(f"   File: {concept3}")
    
    print("=" * 60)
    print("🎯 All professional logo concepts created!")
    print("\n📁 Files saved as SVG (scalable vector graphics):")
    print("   - lemmik_concept_1_structural_network.svg")
    print("   - lemmik_concept_2_apex_keystone.svg")  
    print("   - lemmik_concept_3_ascending_blueprint.svg")
    print("\n💡 SVG files can be:")
    print("   - Opened in web browsers")
    print("   - Converted to PNG for presentations")
    print("   - Used directly on websites")
    print("   - Scaled to any size without quality loss")

if __name__ == "__main__":
    create_all_professional_logos()
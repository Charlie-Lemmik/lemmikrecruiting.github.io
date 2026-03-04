#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np

def create_logo_concept_1():
    """The Builder - Hard hat with gear"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    
    # Hard hat shape
    hat = patches.Arc((1, 1), 1.5, 1.2, angle=0, theta1=0, theta2=180, 
                      linewidth=3, color='#1e3a8a', fill=False)
    ax.add_patch(hat)
    
    # Gear inside
    gear_center = Circle((1, 0.8), 0.3, color='#f97316', alpha=0.8)
    ax.add_patch(gear_center)
    
    # Text
    ax.text(2.5, 1.2, 'LEMMIK', fontsize=24, fontweight='bold', color='#1e3a8a')
    ax.text(2.5, 0.8, 'CONSTRUCTION RECRUITING', fontsize=12, color='#374151')
    ax.text(2.5, 0.4, 'Building Teams. Building Futures.', fontsize=10, 
            color='#6b7280', style='italic')
    
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('CONCEPT 1: THE BUILDER', pad=20)
    plt.tight_layout()
    plt.savefig('logo_concept_1_builder.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_logo_concept_2():
    """The Connector - Crane handshake"""
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    
    # Left crane
    ax.plot([1, 1], [0.5, 3], linewidth=4, color='#64748b')
    ax.plot([1, 2.5], [2.5, 2.5], linewidth=3, color='#64748b')
    
    # Right crane  
    ax.plot([4, 4], [0.5, 3], linewidth=4, color='#64748b')
    ax.plot([2.5, 4], [2.5, 2.5], linewidth=3, color='#64748b')
    
    # Connection point
    connection = Circle((2.5, 2.5), 0.15, color='#22c55e')
    ax.add_patch(connection)
    
    # Text
    ax.text(2.5, 1.8, 'LEMMIK', fontsize=20, fontweight='bold', 
            color='#64748b', ha='center')
    ax.text(2.5, 1.4, 'CONSTRUCTION RECRUITING', fontsize=10, 
            color='#374151', ha='center')
    ax.text(2.5, 0.8, 'Connecting Talent with Opportunity', fontsize=8, 
            color='#6b7280', style='italic', ha='center')
    
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('CONCEPT 2: THE CONNECTOR', pad=20)
    plt.tight_layout()
    plt.savefig('logo_concept_2_connector.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_logo_concept_3():
    """The Foundation - L-beam"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    
    # I-beam L shape
    l_beam = Polygon([(0.5, 0.5), (0.5, 2.5), (1, 2.5), (1, 1), 
                      (2, 1), (2, 0.5)], closed=True, 
                     facecolor='#374151', edgecolor='#fbbf24', linewidth=2)
    ax.add_patch(l_beam)
    
    # Text
    ax.text(3, 1.8, 'LEMMIK', fontsize=24, fontweight='bold', color='#374151')
    ax.text(3, 1.4, 'CONSTRUCTION RECRUITING', fontsize=12, color='#6b7280')
    ax.text(3, 1.0, 'Your Foundation for Success', fontsize=10, 
            color='#fbbf24', style='italic')
    
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('CONCEPT 3: THE FOUNDATION', pad=20)
    plt.tight_layout()
    plt.savefig('logo_concept_3_foundation.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_logo_concept_4():
    """The Network - Hexagonal pattern"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    
    # Hexagonal network
    hex_centers = [(0.8, 1.5), (1.4, 1.1), (1.4, 1.9), (2.0, 1.5)]
    
    for center in hex_centers:
        hex_shape = patches.RegularPolygon(center, 6, 0.25, 
                                         facecolor='#06b6d4', alpha=0.7,
                                         edgecolor='#1e40af')
        ax.add_patch(hex_shape)
    
    # Connection lines
    for i in range(len(hex_centers)-1):
        ax.plot([hex_centers[i][0], hex_centers[i+1][0]], 
               [hex_centers[i][1], hex_centers[i+1][1]], 
               linewidth=2, color='#1e40af', alpha=0.5)
    
    # Text
    ax.text(3, 1.8, 'LEMMIK', fontsize=22, fontweight='bold', color='#1e40af')
    ax.text(3, 1.4, 'CONSTRUCTION RECRUITING', fontsize=11, color='#374151')
    ax.text(3, 1.0, 'Smart Recruiting. Strong Results.', fontsize=10, 
            color='#06b6d4', style='italic')
    
    ax.set_xlim(0, 6.5)
    ax.set_ylim(0.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('CONCEPT 4: THE NETWORK', pad=20)
    plt.tight_layout()
    plt.savefig('logo_concept_4_network.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_logo_concept_5():
    """The Professional - Triangle with arrow"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 4))
    
    # Triangle/pyramid base
    triangle = Polygon([(1, 0.8), (1.8, 2), (0.2, 2)], closed=True,
                      facecolor='#166534', alpha=0.8)
    ax.add_patch(triangle)
    
    # Upward arrow
    arrow = patches.FancyArrowPatch((1, 1.6), (1, 2.4),
                                  arrowstyle='->', mutation_scale=20,
                                  color='#94a3b8', linewidth=3)
    ax.add_patch(arrow)
    
    # Text
    ax.text(2.5, 1.8, 'LEMMIK', fontsize=22, fontweight='bold', 
            color='#166534', family='serif')
    ax.text(2.5, 1.4, 'CONSTRUCTION RECRUITING', fontsize=11, 
            color='#374151', family='serif')
    ax.text(2.5, 1.0, 'Excellence in Executive Placement', fontsize=10, 
            color='#94a3b8', style='italic', family='serif')
    
    ax.set_xlim(0, 6.5)
    ax.set_ylim(0.5, 2.8)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('CONCEPT 5: THE PROFESSIONAL', pad=20)
    plt.tight_layout()
    plt.savefig('logo_concept_5_professional.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_all_logos():
    """Create all logo concepts"""
    print("🎨 Creating Lemmik Construction Recruiting Logo Concepts...")
    
    create_logo_concept_1()
    print("✅ Created Concept 1: The Builder")
    
    create_logo_concept_2()
    print("✅ Created Concept 2: The Connector")
    
    create_logo_concept_3()
    print("✅ Created Concept 3: The Foundation")
    
    create_logo_concept_4()
    print("✅ Created Concept 4: The Network")
    
    create_logo_concept_5()
    print("✅ Created Concept 5: The Professional")
    
    print("\n🎯 All logo concepts saved as PNG files!")
    print("📁 Files created:")
    print("   - logo_concept_1_builder.png")
    print("   - logo_concept_2_connector.png")
    print("   - logo_concept_3_foundation.png")
    print("   - logo_concept_4_network.png")
    print("   - logo_concept_5_professional.png")

if __name__ == "__main__":
    create_all_logos()
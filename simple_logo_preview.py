#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np

def create_simple_logo_previews():
    """Create simple visual previews of all 5 logo concepts"""
    
    # Set up the figure with 5 subplots
    fig, axes = plt.subplots(5, 1, figsize=(12, 20))
    
    # CONCEPT 1: THE BUILDER
    ax1 = axes[0]
    # Hard hat outline
    hat = patches.Arc((2, 2), 2, 1.5, angle=0, theta1=0, theta2=180, 
                      linewidth=4, color='#1e3a8a')
    ax1.add_patch(hat)
    # Gear inside
    gear = Circle((2, 1.8), 0.4, color='#f97316', alpha=0.8)
    ax1.add_patch(gear)
    # Text
    ax1.text(4, 2.3, 'LEMMIK', fontsize=28, fontweight='bold', color='#1e3a8a')
    ax1.text(4, 1.8, 'CONSTRUCTION RECRUITING', fontsize=14, color='#374151')
    ax1.text(4, 1.3, 'Building Teams. Building Futures.', fontsize=11, 
            color='#6b7280', style='italic')
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 4)
    ax1.set_title('CONCEPT 1: THE BUILDER - Hard hat with gear (Blue/Orange)', 
                  fontsize=16, pad=15)
    ax1.axis('off')
    
    # CONCEPT 2: THE CONNECTOR  
    ax2 = axes[1]
    # Left crane
    ax2.plot([1.5, 1.5], [1, 3.5], linewidth=6, color='#64748b')
    ax2.plot([1.5, 2.5], [3, 3], linewidth=4, color='#64748b')
    # Right crane
    ax2.plot([3.5, 3.5], [1, 3.5], linewidth=6, color='#64748b')
    ax2.plot([2.5, 3.5], [3, 3], linewidth=4, color='#64748b')
    # Connection point
    connection = Circle((2.5, 3), 0.2, color='#22c55e')
    ax2.add_patch(connection)
    # Text
    ax2.text(5, 2.8, 'LEMMIK', fontsize=28, fontweight='bold', color='#64748b')
    ax2.text(5, 2.3, 'CONSTRUCTION RECRUITING', fontsize=14, color='#374151')
    ax2.text(5, 1.8, 'Connecting Talent with Opportunity', fontsize=11, 
            color='#6b7280', style='italic')
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 4)
    ax2.set_title('CONCEPT 2: THE CONNECTOR - Cranes forming handshake (Gray/Green)', 
                  fontsize=16, pad=15)
    ax2.axis('off')
    
    # CONCEPT 3: THE FOUNDATION
    ax3 = axes[2]
    # I-beam L shape
    l_beam = Polygon([(1, 1), (1, 3.5), (1.6, 3.5), (1.6, 1.6), 
                      (3, 1.6), (3, 1)], closed=True, 
                     facecolor='#374151', edgecolor='#fbbf24', linewidth=3)
    ax3.add_patch(l_beam)
    # Text
    ax3.text(4, 2.8, 'LEMMIK', fontsize=28, fontweight='bold', color='#374151')
    ax3.text(4, 2.3, 'CONSTRUCTION RECRUITING', fontsize=14, color='#6b7280')
    ax3.text(4, 1.8, 'Your Foundation for Success', fontsize=11, 
            color='#fbbf24', style='italic')
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 4)
    ax3.set_title('CONCEPT 3: THE FOUNDATION - L-beam structure (Charcoal/Gold)', 
                  fontsize=16, pad=15)
    ax3.axis('off')
    
    # CONCEPT 4: THE NETWORK
    ax4 = axes[3]
    # Network nodes
    nodes = [(1.5, 2.5), (2.2, 2), (2.2, 3), (2.9, 2.5)]
    for node in nodes:
        circle = Circle(node, 0.3, color='#06b6d4', alpha=0.8)
        ax4.add_patch(circle)
    # Connection lines
    for i in range(len(nodes)-1):
        ax4.plot([nodes[i][0], nodes[i+1][0]], 
               [nodes[i][1], nodes[i+1][1]], 
               linewidth=3, color='#1e40af', alpha=0.6)
    # Text
    ax4.text(4, 2.8, 'LEMMIK', fontsize=28, fontweight='bold', color='#1e40af')
    ax4.text(4, 2.3, 'CONSTRUCTION RECRUITING', fontsize=14, color='#374151')
    ax4.text(4, 1.8, 'Smart Recruiting. Strong Results.', fontsize=11, 
            color='#06b6d4', style='italic')
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 4)
    ax4.set_title('CONCEPT 4: THE NETWORK - Connected nodes (Navy/Cyan)', 
                  fontsize=16, pad=15)
    ax4.axis('off')
    
    # CONCEPT 5: THE PROFESSIONAL
    ax5 = axes[4]
    # Triangle/pyramid
    triangle = Polygon([(1.5, 1.5), (2.5, 3.5), (0.5, 3.5)], closed=True,
                      facecolor='#166534', alpha=0.8)
    ax5.add_patch(triangle)
    # Upward arrow
    ax5.arrow(1.5, 2.8, 0, 0.6, head_width=0.2, head_length=0.1, 
             fc='#94a3b8', ec='#94a3b8', linewidth=2)
    # Text
    ax5.text(4, 2.8, 'LEMMIK', fontsize=28, fontweight='bold', 
            color='#166534', family='serif')
    ax5.text(4, 2.3, 'CONSTRUCTION RECRUITING', fontsize=14, 
            color='#374151', family='serif')
    ax5.text(4, 1.8, 'Excellence in Executive Placement', fontsize=11, 
            color='#94a3b8', style='italic', family='serif')
    ax5.set_xlim(0, 10)
    ax5.set_ylim(0, 4)
    ax5.set_title('CONCEPT 5: THE PROFESSIONAL - Pyramid with arrow (Forest/Silver)', 
                  fontsize=16, pad=15)
    ax5.axis('off')
    
    plt.tight_layout()
    plt.savefig('lemmik_all_logo_concepts.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("🎨 Created comprehensive logo concept preview!")
    print("📁 Saved as: lemmik_all_logo_concepts.png")

if __name__ == "__main__":
    create_simple_logo_previews()
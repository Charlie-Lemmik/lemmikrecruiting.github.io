#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np
import math

def create_nano_logo_preview():
    """Create preview grid of all 10 Nano Banana Pro logos"""
    
    fig, axes = plt.subplots(2, 5, figsize=(25, 10))
    fig.suptitle('LEMMIK CONSTRUCTION RECRUITING\n10 Logo Concepts by Nano Banana Pro AI\nForest Green (#1E5128)', 
                 fontsize=18, fontweight='bold', y=0.95)
    
    forest_green = '#1E5128'
    axes = axes.flatten()
    
    concept_names = [
        "1. The Rising Cityscape\n(Building Silhouette)",
        "2. The Keystone Link\n(Crucial Connection)", 
        "3. The Geometric Compass\n(Precision Engineering)",
        "4. The Modular Arrow\n(Growth Progress)",
        "5. The I-Beam Monogram\n(Industrial Strength)",
        "6. The Blueprint Grid\n(Architectural Planning)",
        "7. The Bridge Span\n(Infrastructure Connection)",
        "8. The Ascending Crane\n(Construction Power)",
        "9. The Human Structure\n(People Building)",
        "10. The Gear Shield\n(Industrial Reliability)"
    ]
    
    # Logo 1: Rising Cityscape
    ax = axes[0]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle)
    # Three bars
    ax.add_patch(Rectangle((0.35, 0.45), 0.08, 0.3, facecolor=forest_green))  # Left
    ax.add_patch(Rectangle((0.46, 0.35), 0.08, 0.45, facecolor=forest_green))  # Center  
    ax.add_patch(Rectangle((0.57, 0.55), 0.08, 0.25, facecolor=forest_green))  # Right
    ax.set_title(concept_names[0], fontsize=11, pad=15)
    
    # Logo 2: Keystone Link
    ax = axes[1]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle)
    # Arch shapes and keystone
    arch1 = patches.Arc((0.35, 0.5), 0.3, 0.6, angle=0, theta1=0, theta2=90, 
                       linewidth=6, color=forest_green)
    ax.add_patch(arch1)
    arch2 = patches.Arc((0.65, 0.5), 0.3, 0.6, angle=0, theta1=90, theta2=180, 
                       linewidth=6, color=forest_green)
    ax.add_patch(arch2)
    ax.add_patch(Rectangle((0.45, 0.15), 0.1, 0.1, facecolor=forest_green))  # Keystone
    ax.set_title(concept_names[1], fontsize=11, pad=15)
    
    # Logo 3: Geometric Compass
    ax = axes[2]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=3)
    ax.add_patch(circle)
    # Compass legs
    ax.plot([0.5, 0.35], [0.25, 0.75], color=forest_green, linewidth=4)
    ax.plot([0.5, 0.65], [0.25, 0.75], color=forest_green, linewidth=4)
    ax.add_patch(Circle((0.5, 0.75), 0.05, fill=False, edgecolor=forest_green, linewidth=3))
    # Arc
    arc = patches.Arc((0.5, 0.7), 0.25, 0.1, angle=0, theta1=180, theta2=360, 
                     linewidth=3, color=forest_green)
    ax.add_patch(arc)
    ax.set_title(concept_names[2], fontsize=11, pad=15)
    
    # Logo 4: Modular Arrow
    ax = axes[3]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle)
    # Three squares and triangle
    ax.add_patch(Rectangle((0.25, 0.65), 0.1, 0.1, facecolor=forest_green))
    ax.add_patch(Rectangle((0.35, 0.55), 0.1, 0.1, facecolor=forest_green))
    ax.add_patch(Rectangle((0.45, 0.45), 0.1, 0.1, facecolor=forest_green))
    triangle = Polygon([(0.55, 0.45), (0.7, 0.5), (0.55, 0.55)], facecolor=forest_green)
    ax.add_patch(triangle)
    ax.set_title(concept_names[3], fontsize=11, pad=15)
    
    # Logo 5: I-Beam Monogram
    ax = axes[4]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=5)
    ax.add_patch(circle)
    # L-shaped I-beam
    ax.add_patch(Rectangle((0.35, 0.25), 0.12, 0.4, facecolor=forest_green))  # Vertical
    ax.add_patch(Rectangle((0.35, 0.55), 0.3, 0.12, facecolor=forest_green))   # Horizontal
    ax.set_title(concept_names[4], fontsize=11, pad=15)
    
    # Logo 6: Blueprint Grid
    ax = axes[5]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=3)
    ax.add_patch(circle)
    # Grid lines
    ax.plot([0.5, 0.5], [0.2, 0.8], color=forest_green, linewidth=2)  # Vertical
    ax.plot([0.2, 0.8], [0.5, 0.5], color=forest_green, linewidth=2)  # Horizontal
    # Center square
    ax.plot([0.4, 0.6, 0.6, 0.4, 0.4], [0.4, 0.4, 0.6, 0.6, 0.4], 
           color=forest_green, linewidth=2)
    ax.add_patch(Circle((0.5, 0.5), 0.06, facecolor=forest_green))
    ax.set_title(concept_names[5], fontsize=11, pad=15)
    
    # Logo 7: Bridge Span
    ax = axes[6]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle)
    # Bridge
    ax.add_patch(Rectangle((0.2, 0.3), 0.06, 0.3, facecolor=forest_green))   # Left pillar
    ax.add_patch(Rectangle((0.74, 0.3), 0.06, 0.3, facecolor=forest_green))  # Right pillar
    # Cable arc
    arc = patches.Arc((0.5, 0.4), 0.6, 0.15, angle=0, theta1=0, theta2=180, 
                     linewidth=4, color=forest_green)
    ax.add_patch(arc)
    ax.plot([0.23, 0.77], [0.55, 0.55], color=forest_green, linewidth=4)  # Deck
    ax.set_title(concept_names[6], fontsize=11, pad=15)
    
    # Logo 8: Ascending Crane
    ax = axes[7]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle)
    # Crane
    ax.plot([0.3, 0.3], [0.2, 0.8], color=forest_green, linewidth=5)    # Mast
    ax.plot([0.3, 0.65], [0.2, 0.15], color=forest_green, linewidth=5)  # Jib
    ax.plot([0.65, 0.65], [0.15, 0.6], color=forest_green, linewidth=3) # Hook line
    ax.add_patch(Rectangle((0.62, 0.6), 0.06, 0.06, facecolor=forest_green))  # Load
    ax.set_title(concept_names[7], fontsize=11, pad=15)
    
    # Logo 9: Human Structure
    ax = axes[8]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle)
    # Human from shapes
    ax.add_patch(Circle((0.5, 0.35), 0.08, facecolor=forest_green))  # Head
    trapezoid = Polygon([(0.42, 0.45), (0.58, 0.45), (0.6, 0.65), (0.4, 0.65)], 
                       facecolor=forest_green)  # Torso
    ax.add_patch(trapezoid)
    ax.add_patch(Rectangle((0.4, 0.67), 0.2, 0.08, facecolor=forest_green))  # Base
    ax.set_title(concept_names[8], fontsize=11, pad=15)
    
    # Logo 10: Gear Shield
    ax = axes[9]
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=5)
    ax.add_patch(circle)
    # Shield shape
    shield = patches.Ellipse((0.5, 0.5), 0.35, 0.5, facecolor=forest_green)
    ax.add_patch(shield)
    # Gear teeth (simplified)
    teeth_positions = [(0.48, 0.2), (0.65, 0.35), (0.65, 0.65), 
                      (0.48, 0.8), (0.35, 0.65), (0.35, 0.35)]
    for x, y in teeth_positions:
        ax.add_patch(Rectangle((x, y), 0.04, 0.04, facecolor=forest_green))
    # Diamond center
    diamond = Polygon([(0.5, 0.4), (0.55, 0.5), (0.5, 0.6), (0.45, 0.5)], 
                     facecolor='white')
    ax.add_patch(diamond)
    ax.set_title(concept_names[9], fontsize=11, pad=15)
    
    # Style all subplots
    for i, ax in enumerate(axes):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Add subtle border
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(1)
            spine.set_color('#E5E5E5')
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.85, hspace=0.3)
    plt.savefig('nano_banana_10_logos_preview.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()
    
    print("🍌 Created Nano Banana Pro logos preview!")
    print("📁 Saved as: nano_banana_10_logos_preview.png")

if __name__ == "__main__":
    create_nano_logo_preview()
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np
import math

def create_logo_preview_grid():
    """Create a grid showing all 10 logos for easy comparison"""
    
    fig, axes = plt.subplots(2, 5, figsize=(20, 8))
    fig.suptitle('LEMMIK CONSTRUCTION RECRUITING - 10 Logo Concepts\nForest Green (#1E5128) - Clean, Geometric Design', 
                 fontsize=16, fontweight='bold')
    
    forest_green = '#1E5128'
    
    # Flatten axes for easier indexing
    axes = axes.flatten()
    
    # Logo 1: Vertical Bars
    ax = axes[0]
    circle1 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle1)
    # Bars
    bars = [(0.35, 0.4, 0.04, 0.2), (0.42, 0.35, 0.04, 0.3), (0.49, 0.3, 0.04, 0.4), 
            (0.56, 0.38, 0.04, 0.25), (0.63, 0.33, 0.04, 0.32)]
    for x, y, w, h in bars:
        ax.add_patch(Rectangle((x, y), w, h, facecolor=forest_green))
    ax.set_title('1. Vertical Bars\n(Building Silhouette)', fontsize=12, pad=10)
    
    # Logo 2: Construction Tools
    ax = axes[1]
    circle2 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle2)
    # Hammer
    ax.add_patch(Rectangle((0.45, 0.3), 0.1, 0.3, facecolor=forest_green))  # Handle
    ax.add_patch(Rectangle((0.4, 0.55), 0.2, 0.1, facecolor=forest_green))  # Head
    ax.set_title('2. Construction Tools\n(Hammer & Wrench)', fontsize=12, pad=10)
    
    # Logo 3: Hexagon Pattern
    ax = axes[2]
    circle3 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle3)
    # Central hexagon
    hex_angles = np.linspace(0, 2*np.pi, 7)
    hex_x = 0.5 + 0.15 * np.cos(hex_angles)
    hex_y = 0.5 + 0.15 * np.sin(hex_angles)
    hex_patch = Polygon(list(zip(hex_x, hex_y)), facecolor=forest_green)
    ax.add_patch(hex_patch)
    ax.set_title('3. Hexagon Pattern\n(Industrial/Molecular)', fontsize=12, pad=10)
    
    # Logo 4: L-Beam
    ax = axes[3]
    circle4 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle4)
    # L-beam
    ax.add_patch(Rectangle((0.35, 0.3), 0.08, 0.4, facecolor=forest_green))  # Vertical
    ax.add_patch(Rectangle((0.35, 0.62), 0.3, 0.08, facecolor=forest_green))  # Horizontal
    ax.set_title('4. L-Beam\n(Structural Steel)', fontsize=12, pad=10)
    
    # Logo 5: Crane
    ax = axes[4]
    circle5 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle5)
    # Crane
    ax.add_patch(Rectangle((0.48, 0.3), 0.04, 0.4, facecolor=forest_green))  # Mast
    ax.add_patch(Rectangle((0.52, 0.35), 0.2, 0.04, facecolor=forest_green))  # Jib
    ax.add_patch(Rectangle((0.35, 0.35), 0.13, 0.04, facecolor=forest_green))  # Counter-jib
    ax.plot([0.7, 0.7], [0.39, 0.6], color=forest_green, linewidth=2)  # Hook line
    ax.set_title('5. Tower Crane\n(Construction Site)', fontsize=12, pad=10)
    
    # Logo 6: Gear
    ax = axes[5]
    circle6 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle6)
    # Gear
    gear_circle = Circle((0.5, 0.5), 0.2, fill=False, edgecolor=forest_green, linewidth=3)
    ax.add_patch(gear_circle)
    # Gear teeth (simplified)
    for i in range(8):
        angle = i * 45 * np.pi / 180
        x = 0.5 + 0.22 * np.cos(angle)
        y = 0.5 + 0.22 * np.sin(angle)
        ax.add_patch(Rectangle((x-0.02, y-0.04), 0.04, 0.08, facecolor=forest_green))
    ax.add_patch(Circle((0.5, 0.5), 0.08, facecolor=forest_green))
    ax.set_title('6. Gear/Cog\n(Machinery/Process)', fontsize=12, pad=10)
    
    # Logo 7: Blueprint
    ax = axes[6]
    circle7 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle7)
    # Building outline
    building = [(0.35, 0.7), (0.35, 0.4), (0.45, 0.35), (0.55, 0.35), (0.65, 0.4), (0.65, 0.7)]
    ax.plot([p[0] for p in building], [p[1] for p in building], color=forest_green, linewidth=3)
    # Internal lines
    ax.plot([0.45, 0.45], [0.35, 0.7], color=forest_green, linewidth=2)
    ax.plot([0.55, 0.55], [0.35, 0.7], color=forest_green, linewidth=2)
    ax.set_title('7. Blueprint\n(Architectural Plans)', fontsize=12, pad=10)
    
    # Logo 8: Triangle
    ax = axes[7]
    circle8 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle8)
    # Triangle
    triangle = Polygon([(0.5, 0.3), (0.35, 0.7), (0.65, 0.7)], facecolor=forest_green)
    ax.add_patch(triangle)
    # Inner triangle (cut-out)
    inner_tri = Polygon([(0.5, 0.42), (0.42, 0.58), (0.58, 0.58)], facecolor='white')
    ax.add_patch(inner_tri)
    ax.set_title('8. Triangle/Pyramid\n(Stability/Foundation)', fontsize=12, pad=10)
    
    # Logo 9: Bridge
    ax = axes[8]
    circle9 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle9)
    # Bridge deck
    ax.add_patch(Rectangle((0.3, 0.52), 0.4, 0.04, facecolor=forest_green))
    # Towers
    ax.add_patch(Rectangle((0.38, 0.35), 0.04, 0.2, facecolor=forest_green))
    ax.add_patch(Rectangle((0.58, 0.35), 0.04, 0.2, facecolor=forest_green))
    # Cables
    ax.plot([0.4, 0.5], [0.35, 0.52], color=forest_green, linewidth=2)
    ax.plot([0.4, 0.3], [0.35, 0.52], color=forest_green, linewidth=2)
    ax.plot([0.6, 0.5], [0.35, 0.52], color=forest_green, linewidth=2)
    ax.plot([0.6, 0.7], [0.35, 0.52], color=forest_green, linewidth=2)
    ax.set_title('9. Cable Bridge\n(Infrastructure)', fontsize=12, pad=10)
    
    # Logo 10: Diamond
    ax = axes[9]
    circle10 = Circle((0.5, 0.5), 0.4, fill=False, edgecolor=forest_green, linewidth=4)
    ax.add_patch(circle10)
    # Diamond
    diamond = Polygon([(0.5, 0.3), (0.7, 0.5), (0.5, 0.7), (0.3, 0.5)], facecolor=forest_green)
    ax.add_patch(diamond)
    # Inner diamond
    inner_diamond = Polygon([(0.5, 0.42), (0.58, 0.5), (0.5, 0.58), (0.42, 0.5)], facecolor='white')
    ax.add_patch(inner_diamond)
    ax.add_patch(Circle((0.5, 0.5), 0.03, facecolor=forest_green))
    ax.set_title('10. Diamond\n(Precision/Quality)', fontsize=12, pad=10)
    
    # Style all subplots
    for i, ax in enumerate(axes):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Add subtle border
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(0.5)
            spine.set_color('#E5E5E5')
    
    plt.tight_layout()
    plt.savefig('lemmik_10_logos_preview_grid.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()
    
    print("🌲 Created comprehensive preview grid!")
    print("📁 Saved as: lemmik_10_logos_preview_grid.png")

if __name__ == "__main__":
    create_logo_preview_grid()
"""
Generate All Publication Figures
=================================
Master script to generate all simulations and visualizations for both papers.
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("="*80)
print("PUBLICATION FIGURE GENERATION")
print("="*80)
print()

# Generate geometric paper figures
print("PART 1: GEOMETRIC INTERPRETATIONS PAPER")
print("-"*80)
from geometric_simulations import generate_all_simulations
generate_all_simulations()

print()

# Generate AI paper figures  
print("PART 2: AI PATTERN DISCOVERY PAPER")
print("-"*80)
from ai_simulations import generate_all_ai_figures
generate_all_ai_figures()

print()
print("="*80)
print("[OK] COMPLETE - ALL FIGURES GENERATED")
print("="*80)
print()
print("Output directory: figures/")
print()
print("Geometric paper figures:")
print("  - lepton_mass_ratios.pdf/png")
print("  - golden_spiral_leptons.pdf/png")
print("  - hadron_masses.pdf/png")
print("  - ckm_angles.pdf/png")
print("  - chirality_mechanism.pdf/png")
print("  - fine_structure_alpha.pdf/png")
print()
print("AI paper figures:")
print("  - ai_architecture.pdf/png")
print("  - ai_discovery_timeline.pdf/png")
print("  - ai_pattern_categories.pdf/png")
print("  - ai_disagreement.pdf/png")
print("  - ai_block_similarity.pdf/png")
print("  - ai_golden_ratio.pdf/png")
print("  - ai_cross_domain.pdf/png")
print()
print("Total: 13 figures in PDF and PNG formats (26 files)")

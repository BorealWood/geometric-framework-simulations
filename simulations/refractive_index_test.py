"""
Simulation 3: Electromagnetic Wave Propagation in Dielectric Media
Tests if refractive index emerges from information propagation resistance
"""

import numpy as np
import matplotlib.pyplot as plt

# Known refractive indices (at ~589 nm, sodium D-line)
materials_data = {
    'Vacuum': {'n_measured': 1.000, 'epsilon_r': 1.000, 'polarizability': 0.0},
    'Air': {'n_measured': 1.000293, 'epsilon_r': 1.00059, 'polarizability': 1.78e-4},
    'Water': {'n_measured': 1.333, 'epsilon_r': 80.1, 'polarizability': 1.45e-3},
    'Glass (Crown)': {'n_measured': 1.52, 'epsilon_r': 6.0, 'polarizability': 2.5e-3},
    'Glass (Flint)': {'n_measured': 1.65, 'epsilon_r': 7.5, 'polarizability': 3.2e-3},
    'Diamond': {'n_measured': 2.417, 'epsilon_r': 5.7, 'polarizability': 5.8e-3},
    'Sapphire': {'n_measured': 1.77, 'epsilon_r': 9.4, 'polarizability': 3.4e-3},
}

def calculate_refractive_index_standard(epsilon_r, mu_r=1.0):
    """Standard formula: n = sqrt(epsilon_rmu_r)"""
    return np.sqrt(epsilon_r * mu_r)

def calculate_refractive_index_info_resistance(polarizability, baseline_resistance=1.0):
    """
    Information-resistance framework prediction
    
    Higher polarizability -> Lower resistance to EM wave propagation
    -> Higher information transfer rate -> Higher refractive index
    
    n = sqrt(1 + alpha/R_baseline)
    where alpha is polarizability, R is baseline resistance
    """
    # Scale polarizability to match refractive index range
    # This is the theoretical prediction we're testing
    scaled_alpha = polarizability / (1e-4)  # Normalize
    n_predicted = np.sqrt(1.0 + scaled_alpha * baseline_resistance)
    return n_predicted

print("="*80)
print("ELECTROMAGNETIC PROPAGATION: Information-Resistance Framework Test")
print("="*80)

print("\nMaterial Tests:")
print("-" * 80)
print(f"{'Material':<20} {'n (measured)':<15} {'n (standard)':<15} {'n (info-R)':<15} {'Error %':<10}")
print("-" * 80)

results = []

for material, data in materials_data.items():
    n_measured = data['n_measured']
    n_standard = calculate_refractive_index_standard(data['epsilon_r'])
    n_info_resistance = calculate_refractive_index_info_resistance(data['polarizability'])
    
    error_standard = abs(n_standard - n_measured) / n_measured * 100
    error_info_r = abs(n_info_resistance - n_measured) / n_measured * 100
    
    print(f"{material:<20} {n_measured:<15.4f} {n_standard:<15.4f} {n_info_resistance:<15.4f} {error_info_r:<10.2f}")
    
    results.append({
        'material': material,
        'n_measured': n_measured,
        'n_standard': n_standard,
        'n_info_r': n_info_resistance,
        'error_standard': error_standard,
        'error_info_r': error_info_r
    })

# Statistical analysis
n_measured = [r['n_measured'] for r in results]
n_standard = [r['n_standard'] for r in results]
n_info_r = [r['n_info_r'] for r in results]

corr_standard = np.corrcoef(n_measured, n_standard)[0, 1]
corr_info_r = np.corrcoef(n_measured, n_info_r)[0, 1]

mean_error_standard = np.mean([r['error_standard'] for r in results])
mean_error_info_r = np.mean([r['error_info_r'] for r in results])

print("\n" + "="*80)
print("RESULTS:")
print("="*80)
print(f"Standard EM Theory:")
print(f"  Correlation: {corr_standard:.4f}")
print(f"  Mean Error: {mean_error_standard:.2f}%")
print()
print(f"Information-Resistance Framework:")
print(f"  Correlation: {corr_info_r:.4f}")
print(f"  Mean Error: {mean_error_info_r:.2f}%")

if corr_info_r > 0.9:
    print("\n[OK] STRONG CORRELATION: Information-resistance predicts refractive indices")
elif corr_info_r > 0.7:
    print("\n[!] MODERATE CORRELATION: Framework partially explains EM propagation")
else:
    print("\n[X] WEAK CORRELATION: Framework does not explain refractive index")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Measured vs Predicted
materials_list = [r['material'] for r in results]
x_pos = np.arange(len(materials_list))

width = 0.35
ax1.bar(x_pos - width/2, n_measured, width, label='Measured', alpha=0.7, edgecolor='black')
ax1.bar(x_pos + width/2, n_info_r, width, label='Info-Resistance', alpha=0.7, edgecolor='black')

ax1.set_xticks(x_pos)
ax1.set_xticklabels(materials_list, rotation=45, ha='right')
ax1.set_ylabel('Refractive Index', fontsize=12)
ax1.set_title('Measured vs Information-Resistance Prediction', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3, axis='y')

# Plot 2: Correlation scatter
ax2.scatter(n_measured, n_info_r, s=100, alpha=0.6, edgecolors='black')
for i, material in enumerate(materials_list):
    ax2.annotate(material, (n_measured[i], n_info_r[i]), fontsize=8, ha='right')

# Perfect agreement line
min_n = min(min(n_measured), min(n_info_r))
max_n = max(max(n_measured), max(n_info_r))
ax2.plot([min_n, max_n], [min_n, max_n], 'k--', alpha=0.5, label='Perfect Agreement')

ax2.set_xlabel('Measured Refractive Index', fontsize=12)
ax2.set_ylabel('Information-Resistance Prediction', fontsize=12)
ax2.set_title(f'Framework Correlation (R={corr_info_r:.3f})', fontsize=14, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('d:/The thought/Tri-Mind-AGI/simulations/refractive_index_results.png', dpi=150, bbox_inches='tight')
print(f"\n[CHART] Visualization saved: refractive_index_results.png")

print("\n" + "="*80)
print("INTERPRETATION:")
print("="*80)
print(f"""
If information-resistance framework is correct:
- Refractive index should emerge from medium's resistance to EM propagation
- Higher polarizability -> Lower resistance -> Faster information transfer
- Should predict n across all materials

Current Results:
- Correlation: {corr_info_r:.4f}
- Mean Error: {mean_error_info_r:.2f}%
- {'[OK] Framework captures EM propagation physics' if corr_info_r > 0.9 else '[!] Framework needs refinement for EM waves'}

Note: Standard EM theory (n=sqrtepsilon_r) correlation: {corr_standard:.4f}
""")

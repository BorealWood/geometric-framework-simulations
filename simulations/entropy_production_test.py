"""
Simulation 2: Entropy Production in Non-Equilibrium Systems
Tests if information dispersal rate = thermodynamic entropy production
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import laplace

# Physical constants (SI units - exact values since 2019 SI redefinition)
k_B = 1.380649e-23  # Boltzmann constant (J/K)
hbar = 1.054571817e-34  # Reduced Planck constant (J·s)
c = 2.99792458e8  # Speed of light (m/s)

def simulate_heat_diffusion(T_hot, T_cold, thermal_conductivity, size=50, timesteps=1000, dt=0.01):
    """Simulate 2D heat diffusion"""
    # Initialize temperature field
    T = np.zeros((size, size))
    T[:, 0] = T_hot  # Hot boundary (left)
    T[:, -1] = T_cold  # Cold boundary (right)
    T[:, 1:-1] = np.linspace(T_hot, T_cold, size-2)  # Initial gradient
    
    # Thermal diffusivity
    alpha = thermal_conductivity / (1.0 * 1000)  # Approximate for materials
    
    entropy_production_thermo = 0
    info_dispersal_rate = 0
    
    for step in range(timesteps):
        # Apply heat equation: d/dT/d/dt = alphanabla^2T
        laplacian = laplace(T)
        T_new = T + alpha * dt * laplacian
        
        # Fixed boundary conditions
        T_new[:, 0] = T_hot
        T_new[:, -1] = T_cold
        
        # Calculate thermodynamic entropy production
        # dS/dt = integral(knablaT^2/T^2) dV
        grad_T_x = np.gradient(T, axis=1)
        grad_T_y = np.gradient(T, axis=0)
        grad_T_squared = grad_T_x**2 + grad_T_y**2
        
        local_entropy_production = thermal_conductivity * grad_T_squared / (T**2 + 1e-10)
        entropy_production_thermo += np.sum(local_entropy_production) * dt
        
        # Calculate information dispersal rate
        # Information density = S_boltzmann = k_B * ln(microstates) proportional to k_B * ln(T)
        info_density = k_B * np.log(T + 1)
        
        # Information flow = nabla(info_density) / resistance
        # Resistance = 1/thermal_conductivity
        grad_info_x = np.gradient(info_density, axis=1)
        grad_info_y = np.gradient(info_density, axis=0)
        
        info_flow = thermal_conductivity * (grad_info_x**2 + grad_info_y**2)
        info_dispersal_rate += np.sum(info_flow) * dt
        
        T = T_new
    
    return T, entropy_production_thermo, info_dispersal_rate

print("="*80)
print("ENTROPY PRODUCTION: Information-Resistance Framework Test")
print("="*80)

# Test different materials
materials = {
    'Copper': 401,      # W/(m·K)
    'Aluminum': 237,
    'Steel': 50,
    'Glass': 1.0,
    'Wood': 0.15,
    'Air': 0.026,
}

print("\nMaterial Tests:")
print("-" * 80)
print(f"{'Material':<15} {'k (W/m·K)':<15} {'Entropy (thermo)':<20} {'Info Dispersal':<20} {'Ratio':<10}")
print("-" * 80)

results = []

for material, k in materials.items():
    T_final, S_thermo, I_info = simulate_heat_diffusion(
        T_hot=373.15,  # 100 degreesC
        T_cold=273.15, # 0 degreesC
        thermal_conductivity=k,
        size=30,
        timesteps=500,
        dt=0.01
    )
    
    # Normalize to compare
    ratio = S_thermo / (I_info + 1e-20)
    
    print(f"{material:<15} {k:<15.3f} {S_thermo:<20.6e} {I_info:<20.6e} {ratio:<10.4f}")
    
    results.append({
        'material': material,
        'k': k,
        'S_thermo': S_thermo,
        'I_info': I_info,
        'ratio': ratio
    })

# Statistical analysis
S_values = [r['S_thermo'] for r in results]
I_values = [r['I_info'] for r in results]
correlation = np.corrcoef(S_values, I_values)[0, 1]

print("\n" + "="*80)
print("RESULTS:")
print("="*80)
print(f"Correlation Coefficient: {correlation:.4f}")
print(f"Mean Ratio (S/I): {np.mean([r['ratio'] for r in results]):.4f}")
print(f"Std Dev Ratio: {np.std([r['ratio'] for r in results]):.4f}")

if correlation > 0.95:
    print("\n[OK] EXCELLENT CORRELATION: Entropy production = Information dispersal")
elif correlation > 0.85:
    print("\n[!] GOOD CORRELATION: Framework mostly correct, minor discrepancies")
else:
    print("\n[X] POOR CORRELATION: Framework needs revision")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Plot 1: Scatter plot
ax = axes[0, 0]
ax.scatter(S_values, I_values, s=100, alpha=0.6, edgecolors='black')
for i, r in enumerate(results):
    ax.annotate(r['material'], (S_values[i], I_values[i]), fontsize=8, ha='right')

# Add trend line
z = np.polyfit(S_values, I_values, 1)
p = np.poly1d(z)
x_line = np.linspace(min(S_values), max(S_values), 100)
ax.plot(x_line, p(x_line), 'r--', alpha=0.5, label=f'Linear Fit (R={correlation:.3f})')

ax.set_xlabel('Thermodynamic Entropy Production', fontsize=12)
ax.set_ylabel('Information Dispersal Rate', fontsize=12)
ax.set_title('Entropy vs Information Dispersal', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 2: Ratio across materials
ax = axes[0, 1]
materials_list = [r['material'] for r in results]
ratios = [r['ratio'] for r in results]
colors = plt.cm.viridis(np.linspace(0, 1, len(materials_list)))

bars = ax.bar(range(len(materials_list)), ratios, color=colors, edgecolor='black', alpha=0.7)
ax.set_xticks(range(len(materials_list)))
ax.set_xticklabels(materials_list, rotation=45, ha='right')
ax.set_ylabel('S_thermo / I_info Ratio', fontsize=12)
ax.set_title('Consistency Across Materials', fontsize=14, fontweight='bold')
ax.axhline(y=np.mean(ratios), color='red', linestyle='--', label=f'Mean = {np.mean(ratios):.2f}')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# Plot 3: Heat map example (Copper)
ax = axes[1, 0]
T_example, _, _ = simulate_heat_diffusion(401, 373.15, 273.15, size=50, timesteps=1000)
im = ax.imshow(T_example, cmap='hot', aspect='auto')
ax.set_title('Temperature Distribution (Copper)', fontsize=14, fontweight='bold')
ax.set_xlabel('Position (x)')
ax.set_ylabel('Position (y)')
plt.colorbar(im, ax=ax, label='Temperature (K)')

# Plot 4: Thermal conductivity vs entropy/info
ax = axes[1, 1]
k_values = [r['k'] for r in results]
ax.loglog(k_values, S_values, 'bo-', label='Thermodynamic Entropy', markersize=8)
ax.loglog(k_values, I_values, 'rs--', label='Information Dispersal', markersize=8)
ax.set_xlabel('Thermal Conductivity (W/m·K)', fontsize=12)
ax.set_ylabel('Rate', fontsize=12)
ax.set_title('Dependence on Material Properties', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3, which='both')

plt.tight_layout()
plt.savefig('d:/The thought/Tri-Mind-AGI/simulations/entropy_production_results.png', dpi=150, bbox_inches='tight')
print(f"\n[CHART] Visualization saved: entropy_production_results.png")

print("\n" + "="*80)
print("INTERPRETATION:")
print("="*80)
print(f"""
If information-resistance framework is correct:
- Thermodynamic entropy production should equal information dispersal
- Should hold across all materials (copper to air)
- Correlation coefficient should be near 1.0

Current Results:
- Correlation: {correlation:.4f}
- {'[OK] Strong correlation observed' if correlation > 0.95 else '[!] Framework requires refinement'}
- Suggests {'thermodynamics IS information dynamics' if correlation > 0.95 else 'relationship exists but incomplete'}
""")

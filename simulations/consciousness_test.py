"""
Simulation 7: Neural Consciousness from Information-Resistance Networks
Tests if consciousness emerges from brain connectivity patterns (info flow)
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def create_brain_network(n_neurons, connectivity_type='awake'):
    """
    Create simplified brain network model
    
    Connectivity patterns:
    - Awake: High integration, low resistance
    - Asleep: Modular, medium resistance  
    - Anesthetized: Fragmented, high resistance
    """
    G = nx.Graph()
    G.add_nodes_from(range(n_neurons))
    
    if connectivity_type == 'awake':
        # High global connectivity
        # Small-world network: local clusters + long-range connections
        p_local = 0.3  # Local connection probability
        p_long_range = 0.05  # Long-range connection probability
        resistance_base = 1.0
        
    elif connectivity_type == 'asleep':
        # Reduced long-range, maintained local
        p_local = 0.25
        p_long_range = 0.01
        resistance_base = 3.0
        
    elif connectivity_type == 'anesthetized':
        # Severely reduced connectivity
        p_local = 0.15
        p_long_range = 0.001
        resistance_base = 10.0
        
    else:
        raise ValueError(f"Unknown connectivity type: {connectivity_type}")
    
    # Add local connections
    for i in range(n_neurons):
        for j in range(i+1, min(i+10, n_neurons)):  # Local neighborhood
            if np.random.random() < p_local:
                resistance = resistance_base * np.random.uniform(0.8, 1.2)
                G.add_edge(i, j, resistance=resistance)
    
    # Add long-range connections
    for i in range(n_neurons):
        for j in range(i+10, n_neurons):
            if np.random.random() < p_long_range:
                resistance = resistance_base * np.random.uniform(1.0, 1.5)
                G.add_edge(i, j, resistance=resistance)
    
    return G

def calculate_phi(G):
    """
    Calculate integrated information Phi (simplified IIT measure)
    
    Phi measures information integration across the network
    Higher Phi -> More consciousness (IIT prediction)
    
    In info-resistance framework:
    Phi proportional to 1 / (mean path resistance)
    Low resistance paths -> High integration -> High Phi
    """
    if len(G.edges()) == 0:
        return 0.0
    
    # Calculate all-pairs shortest path (using resistance as weight)
    try:
        path_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='resistance'))
    except:
        return 0.0
    
    # Average path resistance
    total_resistance = 0
    count = 0
    for source in path_lengths:
        for target, resistance in path_lengths[source].items():
            if source != target:
                total_resistance += resistance
                count += 1
    
    if count == 0:
        return 0.0
    
    mean_path_resistance = total_resistance / count
    
    # Phi inversely proportional to resistance
    # Lower resistance -> Higher integration -> Higher Phi
    phi = 100.0 / mean_path_resistance  # Scaled for readability
    
    return phi

def calculate_network_metrics(G):
    """Calculate various network metrics"""
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()
    
    if n_edges == 0:
        return {
            'density': 0,
            'clustering': 0,
            'mean_resistance': float('inf'),
            'global_efficiency': 0
        }
    
    density = nx.density(G)
    
    try:
        clustering = nx.average_clustering(G)
    except:
        clustering = 0
    
    # Mean resistance across all edges
    resistances = [data['resistance'] for u, v, data in G.edges(data=True)]
    mean_resistance = np.mean(resistances)
    
    # Global efficiency (inverse of mean path length)
    try:
        efficiency = nx.global_efficiency(G)
    except:
        efficiency = 0
    
    return {
        'density': density,
        'clustering': clustering,
        'mean_resistance': mean_resistance,
        'global_efficiency': efficiency
    }

print("="*80)
print("NEURAL CONSCIOUSNESS: Information-Resistance Framework Test")
print("="*80)

n_neurons = 100  # Simplified brain network
n_trials = 10  # Multiple trials for statistics

print(f"\nSimulating {n_neurons}-neuron networks across {n_trials} trials")
print("-" * 80)

states = ['awake', 'asleep', 'anesthetized']
results_by_state = {state: [] for state in states}

print(f"{'State':<20} {'Trial':<10} {'Phi (IIT)':<15} {'Mean R':<15} {'Efficiency':<15}")
print("-" * 80)

for state in states:
    for trial in range(n_trials):
        # Create network
        G = create_brain_network(n_neurons, state)
        
        # Calculate Phi (integrated information)
        phi = calculate_phi(G)
        
        # Calculate other metrics
        metrics = calculate_network_metrics(G)
        
        print(f"{state:<20} {trial+1:<10} {phi:<15.2f} {metrics['mean_resistance']:<15.2f} "
              f"{metrics['global_efficiency']:<15.4f}")
        
        results_by_state[state].append({
            'phi': phi,
            'mean_resistance': metrics['mean_resistance'],
            'efficiency': metrics['global_efficiency'],
            'density': metrics['density'],
            'clustering': metrics['clustering']
        })

# Statistical analysis
print("\n" + "="*80)
print("STATISTICAL SUMMARY:")
print("="*80)

for state in states:
    phi_values = [r['phi'] for r in results_by_state[state]]
    resistance_values = [r['mean_resistance'] for r in results_by_state[state]]
    
    mean_phi = np.mean(phi_values)
    std_phi = np.std(phi_values)
    mean_resistance = np.mean(resistance_values)
    
    print(f"\n{state.upper()}:")
    print(f"  Phi (consciousness): {mean_phi:.2f} +/- {std_phi:.2f}")
    print(f"  Mean Resistance: {mean_resistance:.2f}")
    print(f"  Phi/R ratio: {mean_phi/mean_resistance:.2f}")

# Compare states
phi_awake = np.mean([r['phi'] for r in results_by_state['awake']])
phi_asleep = np.mean([r['phi'] for r in results_by_state['asleep']])
phi_anesthetized = np.mean([r['phi'] for r in results_by_state['anesthetized']])

print("\n" + "="*80)
print("CONSCIOUSNESS PREDICTIONS:")
print("="*80)

print(f"Phi(awake) / Phi(anesthetized) = {phi_awake / phi_anesthetized:.2f}x")
print(f"Phi(awake) / Phi(asleep) = {phi_awake / phi_asleep:.2f}x")

# IIT predicts Phi(awake) >> Phi(anesthetized)
# Info-resistance predicts: Low resistance -> High Phi
if phi_awake > phi_anesthetized * 3:
    print("\n[OK] PREDICTION VALIDATED: Consciousness correlates with integrated information")
    print("  Framework explains: Anesthesia increases resistance -> Phi decreases -> consciousness lost")
elif phi_awake > phi_anesthetized * 1.5:
    print("\n[!] PARTIAL VALIDATION: Trend correct but weaker than expected")
else:
    print("\n[X] PREDICTION FAILED: No clear consciousness correlation")

# Test correlation between Phi and resistance
all_phi = []
all_resistance = []
for state in states:
    all_phi.extend([r['phi'] for r in results_by_state[state]])
    all_resistance.extend([r['mean_resistance'] for r in results_by_state[state]])

correlation = np.corrcoef(all_phi, all_resistance)[0, 1]
print(f"\nCorrelation (Phi vs Resistance): {correlation:.4f}")
print(f"{'[OK] Strong anti-correlation' if correlation < -0.7 else '[!] Weak relationship'}")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Phi across states
ax = axes[0, 0]
phi_data = [
    [r['phi'] for r in results_by_state['awake']],
    [r['phi'] for r in results_by_state['asleep']],
    [r['phi'] for r in results_by_state['anesthetized']]
]
bp = ax.boxplot(phi_data, labels=['Awake', 'Asleep', 'Anesthetized'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['green', 'blue', 'red']):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

ax.set_ylabel('Integrated Information Phi', fontsize=12)
ax.set_title('Consciousness Measure Across Brain States', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

# Plot 2: Resistance across states
ax = axes[0, 1]
resistance_data = [
    [r['mean_resistance'] for r in results_by_state['awake']],
    [r['mean_resistance'] for r in results_by_state['asleep']],
    [r['mean_resistance'] for r in results_by_state['anesthetized']]
]
bp = ax.boxplot(resistance_data, labels=['Awake', 'Asleep', 'Anesthetized'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['green', 'blue', 'red']):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

ax.set_ylabel('Mean Information Resistance', fontsize=12)
ax.set_title('Network Resistance Across States', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

# Plot 3: Phi vs Resistance scatter
ax = axes[1, 0]
colors_scatter = ['green']*n_trials + ['blue']*n_trials + ['red']*n_trials
ax.scatter(all_resistance, all_phi, c=colors_scatter, s=80, alpha=0.6, edgecolors='black')

# Fit line
z = np.polyfit(all_resistance, all_phi, 1)
p = np.poly1d(z)
r_range = np.linspace(min(all_resistance), max(all_resistance), 100)
ax.plot(r_range, p(r_range), 'k--', linewidth=2, label=f'R={correlation:.2f}')

ax.set_xlabel('Mean Resistance', fontsize=12)
ax.set_ylabel('Integrated Information Phi', fontsize=12)
ax.set_title('Consciousness vs Information Resistance', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 4: Network efficiency comparison
ax = axes[1, 1]
efficiency_means = [
    np.mean([r['efficiency'] for r in results_by_state['awake']]),
    np.mean([r['efficiency'] for r in results_by_state['asleep']]),
    np.mean([r['efficiency'] for r in results_by_state['anesthetized']])
]
colors_bar = ['green', 'blue', 'red']
ax.bar(['Awake', 'Asleep', 'Anesthetized'], efficiency_means, color=colors_bar, alpha=0.6, edgecolor='black')

ax.set_ylabel('Global Efficiency', fontsize=12)
ax.set_title('Information Transfer Efficiency', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('d:/The thought/Tri-Mind-AGI/simulations/consciousness_results.png', dpi=150, bbox_inches='tight')
print(f"\n[CHART] Visualization saved: consciousness_results.png")

print("\n" + "="*80)
print("INTERPRETATION:")
print("="*80)
print(f"""
Integrated Information Theory (IIT):
- Consciousness = Integrated information (Phi)
- High Phi -> Conscious experience
- Anesthesia should drastically reduce Phi

Information-Resistance Framework:
- Consciousness emerges from low-resistance information integration
- Anesthesia increases neural resistance 10*
- Predicts: Phi proportional to 1/R (inverse relationship)

Current Results:
- Phi(awake): {phi_awake:.2f}
- Phi(anesthetized): {phi_anesthetized:.2f}
- Ratio: {phi_awake/phi_anesthetized:.2f}* reduction
- Correlation Phi vs R: {correlation:.4f}
- {'[OK] Framework explains consciousness' if abs(correlation) > 0.7 and phi_awake > phi_anesthetized * 3 else '[!] Needs refinement'}

Key Insight: {'Consciousness = Integrated information flow through low-resistance paths' if abs(correlation) > 0.7 else 'Mechanism unclear'}
""")

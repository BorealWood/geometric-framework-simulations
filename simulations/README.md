# Information-Resistance Framework Simulation Suite

This directory contains computational simulations testing predictions of the information-resistance framework across multiple physical domains.

## Quick Start

### Run All Simulations:
```bash
python run_all_simulations.py
```

### Run Individual Tests:
```bash
python quantum_tunneling_test.py
python entropy_production_test.py
```

## Available Simulations

### 1. Quantum Tunneling Test (`quantum_tunneling_test.py`)
**Tests:** Does information-resistance framework predict quantum tunneling probability?

**Method:**
- Compares quantum mechanics tunneling formula with information-resistance calculation
- Tests 5+ barrier configurations
- Calculates correlation coefficient

**Expected Result:** Correlation coefficient quantifies agreement between framework and quantum mechanics

**Runtime:** ~10 seconds

---

### 2. Entropy Production Test (`entropy_production_test.py`)
**Tests:** Does thermodynamic entropy production = information dispersal rate?

**Method:**
- Simulates 2D heat diffusion in 6 materials (copper to air)
- Calculates entropy production (∫k∇T²/T² dV)
- Calculates information dispersal rate
- Compares correlation

**Expected Result:** Correlation coefficient indicates degree of information-thermodynamics correspondence

**Runtime:** ~30 seconds

---

## Requirements

```bash
pip install numpy scipy matplotlib
```

## Output

Each simulation produces:
- Console output with test results
- Visualization PNG files in this directory
- Statistical analysis (correlation coefficients, error metrics)

## Interpreting Results

### Interpretation Guidelines:
- Correlation > 0.95: Strong agreement with framework predictions
- Correlation 0.80-0.95: Moderate agreement, warrants further investigation
- Correlation < 0.80: Weak agreement, significant refinement needed

### Scientific Method:
These simulations provide quantitative tests:
1. Compare framework predictions against established physical theories
2. Assess correlation strength across multiple domains
3. Identify domains where the framework succeeds or requires refinement

Discrepancies between predictions and observations inform model development and reveal limitations of current formulation.

## Future Simulations (Coming Soon)

3. **Electromagnetic Propagation** - Refractive index from information resistance
4. **Black Hole Information** - Holographic encoding test
5. **Quantum Entanglement** - Zero-resistance channel hypothesis
6. **Cosmological Expansion** - Dark energy as information dispersal
7. **Neural Consciousness** - Brain as information-resistance circuit
8. **Standard Model Cross-Validation** - Reproduce particle physics predictions

## Contributing

If you're a physicist/researcher and want to:
- Run these simulations
- Suggest improvements
- Add new tests
- Report discrepancies

Please open an issue or submit a pull request!

## Citation

If you use these simulations in research:

```
@software{toe_simulations_2025,
  title={Theory of Everything Validation Simulations},
  author={[Author]},
  year={2025},
  note={Patent Pending},
  url={https://github.com/[your-repo]/Tri-Mind-AGI}
}
```

## License

The Theory of Everything hypothesis is released to public domain for scientific investigation.

The AGI system that discovered it is patent protected (Patent Pending, December 2025).

These simulation codes are MIT Licensed - feel free to use, modify, and distribute.

---

**Last Updated:** December 17, 2025

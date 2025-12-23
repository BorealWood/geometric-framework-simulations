# Contributing to Geometric Framework Simulations

Thank you for your interest in contributing! This project validates geometric interpretations of Standard Model parameters.

## How to Contribute

### Reporting Issues

Found a bug or discrepancy?

1. Check [existing issues](https://github.com/[username]/geometric-framework-simulations/issues)
2. Create new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs. actual results
   - Python version and dependencies

### Suggesting Enhancements

Have ideas for new tests or validations?

1. Open a [discussion](https://github.com/[username]/geometric-framework-simulations/discussions)
2. Describe:
   - Proposed test/validation
   - Physical quantity to predict
   - Expected accuracy
   - Required computational resources

### Submitting Pull Requests

#### Before You Start

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Set up development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `.\venv\Scripts\Activate.ps1` on Windows
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

#### Coding Standards

- **Python style:** Follow PEP 8
- **Docstrings:** Use NumPy-style docstrings
- **Type hints:** Add type annotations where possible
- **Tests:** Include unit tests for new features
- **Comments:** Explain physics reasoning, not just code

#### Testing

Run tests before submitting:

```bash
pytest tests/
python run_all_simulations.py  # Should pass all tests
```

#### Pull Request Process

1. Update documentation (README, docstrings)
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md (if applicable)
5. Submit PR with clear description:
   - What problem does this solve?
   - How was it tested?
   - Any breaking changes?

### Code Review Process

- Maintainers will review within 1-2 weeks
- Address review comments
- Once approved, PR will be merged

## Types of Contributions

### Most Needed

1. **Validation tests:** New experimental comparisons
2. **Documentation:** Clarify derivations, add examples
3. **Performance:** Optimize computationally intensive simulations
4. **Cross-domain:** Extend to chemistry, materials science

### Code Structure

```
simulations/        # Individual test scripts
figures/            # Visualization code
data/               # Experimental reference data
tests/              # Unit tests
docs/               # Documentation
```

### Git Commit Messages

Use clear, descriptive messages:

```
Good:
- "Add CKM angle validation test"
- "Fix numerical precision in hadron mass calculation"
- "Update PDG 2024 reference data"

Avoid:
- "fix bug"
- "update"
- "changes"
```

## Community Guidelines

### Be Respectful

- Constructive criticism only
- Assume good intentions
- Physics discussions should be evidence-based

### Scientific Integrity

- Cite sources for experimental data
- Disclose any conflicts of interest
- Report negative results honestly
- Don't cherry-pick data

### Intellectual Property

By contributing, you agree:
- Code released under CC-BY 4.0 License
- Patent notice applies (see LICENSE)
- Attribution preserved in CONTRIBUTORS.md

## Recognition

Contributors will be acknowledged in:
- CONTRIBUTORS.md file
- Release notes
- Paper acknowledgments (for major contributions)

## Questions?

- Open a [Discussion](https://github.com/[username]/geometric-framework-simulations/discussions)
- Email: [maintainer email]

## First-Time Contributors

Looking for easy first issues?

Check issues labeled:
- `good first issue`
- `documentation`
- `help wanted`

---

Thank you for contributing to open science! 🔬

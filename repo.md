# ML From Scratch - Project Architecture

A repository for implementing classical machine learning algorithms from scratch using NumPy, while documenting the mathematics, experiments, and software engineering behind each algorithm.

---

# Project Structure

```text
ml-from-scratch/
│
├── linear_models/
│   ├── linear_regression.py
│   ├── logistic_regression.py
│   ├── ridge.py
│   ├── lasso.py
│   └── elastic_net.py
│
├── trees/
├── neighbors/
├── svm/
├── decomposition/
├── clustering/
├── optimization/
│
├── notebooks/
├── docs/
├── tests/
├── benchmarks/
├── examples/
├── datasets/
├── utils/
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── LICENSE
```

---

# Folder Responsibilities

## `linear_models/`

Contains only the implementation of the algorithms.

Responsibilities:

- Clean production-quality code
- `fit()`
- `predict()`
- `score()`
- Internal helper methods

No derivations.

No experiments.

No plots.

Example:

```python
model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)
```

---

## `notebooks/`

The research and learning area.

Every algorithm should have one notebook.

Example:

```text
01_linear_regression.ipynb
02_logistic_regression.ipynb
03_ridge.ipynb
...
```

A notebook should include:

- Motivation
- Mathematical derivation
- Loss function
- Gradient derivation
- Synthetic data generation
- Implementation walkthrough
- Visualizations
- Experiments
- Comparison with scikit-learn
- Discussion
- References

Think of these as interactive lecture notes.

---

## `docs/`

Polished documentation.

Each algorithm has its own document.

Example:

```text
docs/
    linear_regression.md
    logistic_regression.md
```

Each document contains:

- Overview
- Mathematical formulation
- Assumptions
- Algorithm summary
- Complexity analysis
- API description
- References

No experimental code.

No long derivations.

This is the documentation someone reads after installing the library.

---

## `tests/`

Automatic correctness verification.

Example:

```text
tests/
    test_linear_regression.py
```

Typical tests:

- Fits successfully
- Correct coefficients on synthetic data
- Correct predictions
- Matches scikit-learn
- Correct output shapes
- Proper error handling
- Edge cases

Run using:

```bash
pytest
```

---

## `benchmarks/`

Performance evaluation.

Example:

```text
benchmark_linear_regression.py
```

Contains:

- Runtime comparisons
- Scaling with dataset size
- Scaling with number of features
- Memory usage (optional)

---

## `examples/`

Small scripts showing how to use the library.

Example:

```python
from ml.linear_models import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
```

---

## `datasets/`

Small datasets used for:

- Examples
- Unit tests
- Demonstrations

Large datasets should be downloaded separately.

---

## `utils/`

Reusable helper functions.

Examples:

- Metrics
- Data generation
- Matrix utilities
- Train/test split

Only include code reused by multiple algorithms.

---

# Development Workflow

For every new algorithm:

1. Study the mathematics.
2. Create a notebook.
3. Implement the algorithm.
4. Write documentation.
5. Write unit tests.
6. Benchmark performance.
7. Add an example.

---

# Example: Linear Regression

```
linear_models/
    linear_regression.py
        ↓
Implementation

notebooks/
    01_linear_regression.ipynb
        ↓
Derivations + Experiments

docs/
    linear_regression.md
        ↓
Theory + Documentation

tests/
    test_linear_regression.py
        ↓
Correctness Verification

benchmarks/
    benchmark_linear_regression.py
        ↓
Performance

examples/
    linear_regression_example.py
        ↓
Usage Example
```

---

# Philosophy

Every algorithm should have:

- ✅ Clean implementation
- ✅ Mathematical explanation
- ✅ Interactive notebook
- ✅ Unit tests
- ✅ Documentation
- ✅ Benchmarks
- ✅ Usage example

The goal is not only to implement machine learning algorithms but also to demonstrate mathematical understanding, software engineering practices, and reproducible experimentation.
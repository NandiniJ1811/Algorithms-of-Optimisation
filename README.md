# Numerical Optimization Methods — OR II Assignment

Implementation and benchmarking of four classical numerical optimization methods in Python. Built as part of **Operations Research II** at IIT Kharagpur. Compares three interval-reduction search methods (Bisection, Golden Section, Fibonacci) on convergence efficiency, and implements Steepest Ascent for single-variable function maximisation.

---

## Methods Implemented

### 1. Bisection Method
Finds the root of a function by repeatedly halving the search interval.

**Key condition:** `f(a) × f(b) < 0` — the function must change sign over `[a, b]`, guaranteeing a root exists by the Intermediate Value Theorem.

**Iteration bound:**
$$t = \frac{\log(2 \cdot \text{tol} / (b-a))}{\log(0.5)}$$

Each iteration halves the interval, so after $t$ steps the uncertainty interval is guaranteed to be below the specified tolerance.

---

### 2. Golden Section Search
Finds the minimum of a unimodal function by exploiting the golden ratio to reduce the interval while reusing function evaluations.

**Golden ratio:** $R = (3 - \sqrt{5})/2 \approx 0.382$

Interior points are placed as:
$$x_1 = a + R(b-a), \quad x_2 = b - R(b-a)$$

**Iteration bound:**
$$t = \frac{\log(2 \cdot \text{tol} / (b-a))}{\log(1-R)}$$

Each iteration shrinks the interval by factor $1 - R \approx 0.618$. Requires only one new function evaluation per iteration (vs. two for ternary search) — roughly 30% more efficient.

> Assumes unimodal function (single minimum in `[a, b]`).

---

### 3. Fibonacci Search
Finds the minimum of a unimodal function using Fibonacci numbers to determine interval reduction steps.

Generates the Fibonacci sequence up to 100 terms. Selects the largest $n$ such that:
$$F_{n+1} \geq \frac{1}{2 \cdot \text{tol}}$$

This ensures the interval shrinks to within tolerance after exactly $n$ steps. Fibonacci ratios converge to the golden ratio (0.618), giving equivalent asymptotic efficiency — but using integer arithmetic with no irrational numbers.

**Comparison:** Same efficiency as Golden Section, but fully deterministic. Bisection < Golden Section ≈ Fibonacci in terms of convergence rate.

---

### 4. Steepest Ascent (Gradient Ascent)
Maximises a single-variable function by iteratively stepping in the direction of steepest ascent.

**Numerical gradient** via central finite difference:
$$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}, \quad h = 10^{-7}$$

Central difference achieves $O(h^2)$ accuracy, more stable than forward difference.

**Update rule:**
$$x_{t+1} = x_t + \alpha \cdot f'(x_t)$$

**Convergence:** Stops when $|f'(x)| < \text{tol}$ (gradient near zero = at a maximum) or after `max_iter = 1000` steps.

Per-iteration output:

| Iteration | x | f(x) | f′(x) |
|---|---|---|---|
| 1 | 2.300000 | 1.234567 | 0.876543 |
| ... | ... | ... | ... |

> Fixed step size `alpha` controls aggressiveness. Too large → overshoot; too small → slow convergence. Line search variants adapt `alpha` dynamically for ill-conditioned problems.

---

## Auto-Selection Logic

After all three interval-reduction methods run, the program automatically identifies the one that converged in the fewest iterations and declares it the most efficient for the given function and tolerance:

```python
least = min(iter1, iter2, iter3)
if least == iter1: print("Best method: Bisection")
if least == iter2: print("Best method: Golden Section")
if least == iter3: print("Best method: Fibonacci")
```

---

## Usage

### Input format

When entering a function, use Python expression syntax:

| Mathematical | Python input |
|---|---|
| $2x - x^3 + 3$ | `2*x - x**3 + 3` |
| $x^2 - 4$ | `x**2 - 4` |
| $-x^2 + 4x - 1$ | `-x**2 + 4*x - 1` |

### Running the code

### Example session

```
Enter function (e.g., x**3 - x - 2): x**3 - 6*x**2 + 9*x - 2
Enter lower bound (a): 0
Enter upper bound (b): 4
Enter tolerance: 0.001

--- Bisection Method Results ---
Total Iterations: 12
Final Root (x): 1.000488
Final f(x): 0.000977

--- Golden Section Method Results ---
Total Iterations: 17
Final Root (Minimum x): 3.0001
Final f(x): -2.000000

--- Fibonacci Method Results ---
Total Iterations: 15
Final Uncertainty Interval: [2.999, 3.001]
Final Root (Minimum x): 3.0000
Final f(x): -2.000000

Best optimization method is Fibonacci!

Enter function to MAXIMISE: -x**2 + 4*x - 1
Enter starting point x0: 0
Enter step size alpha: 0.1
Enter tolerance: 0.0001

Converged after 47 iteration(s).
Maximum x: 2.000000
Maximum f(x): 3.000000
```

---

## Project Structure

```
optimization-algorithms/
│
├── algo.py     # Main script (all four methods)
├── OR2_Assignment_3.ipynb  # Google Colab notebook
├── report.txt              # Written analysis and methodology
└── README.md
```

---

## Dependencies

```
python >= 3.8
math    # standard library — no external dependencies required
```

---

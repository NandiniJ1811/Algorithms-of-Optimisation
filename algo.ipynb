import math

func_str = input("Enter function in terms of x (e.g., x**3 - x - 2, 2*x - x**2): ")
a = float(input("Enter lower bound (a): "))
b = float(input("Enter upper bound (b): "))
tol = float(input("Enter tolerance (e.g., 0.001): "))

"""### Bisection Method"""

def bisection_method(func_str, a, b, tol):
    f = lambda x: eval(func_str)
    if f(a) * f(b) > 0:
        print("Error: f(a) and f(b) must have opposite signs. No root guaranteed.")
        return

    iteration1 = 0
    t = (math.log(2*tol/(b-a))) / math.log(0.5)

    while iteration1 < t:
        iteration1 += 1
        c = (a + b) / 2

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    final_answer = (a + b) / 2
    fv = f(final_answer)

    print("\n--- Bisection Method Results ---")
    print(f"Total Iterations: {iteration1}")
    print(f"Last Uncertainty Interval: [{a}, {b}]")
    print(f"Final Root (x): {final_answer:.6f}")
    print(f"Final answer : {fv:.6f}")
    return(iteration1)

iter1=bisection_method(func_str, a, b, tol)

"""### Golden Section Method"""

def golden_section_search(func_str, a, b, tol):
    f = lambda x: eval(func_str)
    R = (3 - math.sqrt(5)) / 2

    x1 = a + R * (b - a)
    x2 = b - R * (b - a)
    f1 = f(x1)
    f2 = f(x2)

    iteration2 = 0
    t = (math.log(2*tol/(b-a))) / math.log(1-R)

    while iteration2 < t:
        iteration2 += 1
        if f1 < f2:
            b = x2          # minimum lies in [a, x2]
            x2 = x1
            f2 = f1
            x1 = a + R * (b - a)
            f1 = f(x1)
        else:
            a = x1          # minimum lies in [x1, b]
            x1 = x2
            f1 = f2
            x2 = b - R * (b - a)
            f2 = f(x2)

    final_answer = (a + b) / 2
    fv = f(final_answer)

    print("\n--- Golden Section Method Results ---")
    print(f"Total Iterations: {iteration2}")
    print(f"Final Uncertainty Interval: [{a}, {b}]")
    print(f"Final Root (Minimum x): {final_answer:.4f}")
    print(f"Final answer : {fv:.6f}")
    return(iteration2)

iter2=golden_section_search(func_str, a, b, tol)

"""### Fibbonacci Method"""

def fibonacci_search(func_str, a, b, tol):
    f = lambda x: eval(func_str)

    fib = [1, 1]
    for i in range(2, 100):
        fib.append(fib[i-1] + fib[i-2])

    n = 0
    for i in range(len(fib)):
        if fib[i] >= 1/(2*tol):
            n = i - 1
            break

    L = b - a
    x1 = a + (1 - (fib[n] / fib[n+1])) * L
    x2 = b - (1 - (fib[n] / fib[n+1])) * L
    f1, f2 = f(x1), f(x2)

    for k in range(n, 1, -1):
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (1 - (fib[k-1] / fib[k])) * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - (1 - (fib[k-1] / fib[k])) * (b - a)
            f2 = f(x2)

    final_answer = (a + b) / 2
    fv = f(final_answer)

    print("\n--- Fibonacci Method Results ---")
    print(f"Total Iterations: {n}")
    print(f"Last Uncertainty Interval: [{a}, {b}]")
    print(f"Final Root (Minimum x): {final_answer:.4f}")
    print(f"Final answer : {fv:.6f}")
    return(n)

iter3=fibonacci_search(func_str, a, b, tol)

print(iter1, iter2, iter3)

values = [iter1, iter2, iter3]
values = [v for v in values if v is not None]

least = min(values)

least=min(values)
if least==iter1:
  print("Best optimization method is Bisection!")
if least==iter2:
  print("Best optimization method is Golden section!")
if least==iter3:
  print("Best optimization method is Fibonacci!")

"""### Steepest Ascent Method"""

def steepest_ascent(func_str, x0, alpha, tol, max_iter=1000):
    f  = lambda x: eval(func_str)
    h  = 1e-7
    df = lambda x: (f(x + h) - f(x - h)) / (2 * h)   # numerical gradient

    x = x0
    iteration = 0

    print("\n--- Steepest Ascent Method ---")
    print(f"{'Iter':>5}  {'x':>14}  {'f(x)':>14}  {'f\'(x)':>14}")
    print("-" * 55)

    while iteration < max_iter:
        iteration += 1
        grad = df(x)
        fx   = f(x)
        print(f"{iteration:>5}  {x:>14.6f}  {fx:>14.6f}  {grad:>14.6f}")

        if abs(grad) < tol:
            print(f"\nConverged after {iteration} iteration(s).")
            break

        x = x + alpha * grad   # step toward steepest ascent

    else:
        print(f"\nReached max iterations ({max_iter}) without convergence.")

    print("\n--- Steepest Ascent Results ---")
    print(f"Total Iterations : {iteration}")
    print(f"Maximum x        : {x:.6f}")
    print(f"Maximum f(x)     : {f(x):.6f}")

# Separate inputs for steepest ascent
sa_func = input("Enter function to MAXIMISE in terms of x (e.g., -x**2 + 4*x - 1): ")
x0      = float(input("Enter starting point x0: "))
alpha   = float(input("Enter step size alpha (e.g., 0.1): "))
sa_tol  = float(input("Enter tolerance (e.g., 0.0001): "))

steepest_ascent(sa_func, x0, alpha, sa_tol)

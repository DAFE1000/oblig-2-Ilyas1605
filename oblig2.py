import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# 1. Definer funksjonen f(x)
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# 2. Definer den deriverte likningen (den vi skal finne nullpunktet til)
# Fra oppgaven: tan⁻¹(x) - 4/(x² + 1) = 0
def derivative_eq(x):
    return np.arctan(x) - 4/(x**2 + 1)

# 3. Finn toppunktet numerisk
# Vi ser på grafen (eller gjetter) at x er rundt 1-2
x_topp = fsolve(derivative_eq, 1.5)[0]
y_topp = f(x_topp)

print(f"Toppunktet er i x = {x_topp:.6f}")
print(f"Funksjonsverdien i toppunktet er y = {y_topp:.6f}")

# 4. Plotting
x_vals = np.linspace(0, 10, 500)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='$f(x) = e^{-x/4} \\cdot \\tan^{-1}(x)$')
plt.plot(x_topp, y_topp, 'ro', label=f'Toppunkt: ({x_topp:.4f}, {y_topp:.4f})')

plt.title('Plot av funksjonen f(x) med markert toppunkt')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
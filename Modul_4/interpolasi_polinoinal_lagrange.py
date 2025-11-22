import numpy as np
import matplotlib.pyplot as plt
# data titik
x  = np.array([1.0, 2.0, 3.0])
y  = np.array([3.0, 8.0, 15.0])
xp = 2.5

#fungsi interpolasi lagrange
def lagrange_interpolation(x, y, xp):
  p = 0.0
  n = len(x)
  for i in range (n):
    L = 1.0
    for j in range(n):
      if j != i:
        L *= (xp - x[j]) / (x[i] - x[j])
    p += y[i] * L
  return p

#hasil
L_value = lagrange_interpolation(x, y, xp)

print("Lagrange f(2.5) = ", L_value)

# ---- Grafik ----- #
x = np.array([1.0, 2.0, 3.0])
y = np.array([3.0, 8.0, 15.0])
plt.plot(x, y)
plt.plot(x, y, 'bo', label='Data') # Titik data
plt.plot(xp, L_value, 'ro', label='Perkiraan')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualisasi Interpolasi Lagrange')
plt.legend()
plt.grid(True)
plt.show()

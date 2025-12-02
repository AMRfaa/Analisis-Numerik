import numpy as np
#mendefinisikan fungsi
def f(x, y):
  return y - x**2 + 1

# mendefinisikan Metode Euler
def euler(x0, y0, h, xn):
  x = x0
  y = y0
  while x < xn:
    y = y + h * f(x, y)
    x = x + h
  return y

# Mendefinisikan Metode Runge-Kutta Orde 4 (RK4)
def RK4(x0, y0, h, xn):
  x = x0
  y = y0
  while x < xn:
   k1 = f(x, y)
   k2 = f(x + h/2, y + h/2 * k1)
   k3 = f(x + h/2, y + h/2 * k2)
   k4 = f(x + h, y + h * k3)
   y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
   x = x + h
  return y

# Mendefinisikan Fungsi Analitik
def f_analitik(x):
  return x**2 + 2*x + 1 - 0.5 * np.exp(x)

# Menghitung nilai y pada x = 0.2
x0 = 0
y0 = 0.5
h  = 0.1
xn = 0.2

y_euler = euler(x0, y0, h, xn)
y_RK4   = RK4(x0, y0, h, xn)
y_eksak = f_analitik(xn)

print ("Hasil Metode Euler              :", y_euler)
print ("Hasil Metode Runge-Kutta Orde 4 :", y_RK4)
print ("Hasil Fungsi Analitik           :", y_eksak)


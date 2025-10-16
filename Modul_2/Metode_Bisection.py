#Menyelesaikan Persamaan Non Linear x^3+x^2-3x-3 dengan Metode bisection  

# Mengimport library yang digunakan  
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter as pc

# Mendefinisikan fungsi  
def f(x): 
    return x**3 + x**2 - 3*x - 3 

# Metode Bisection 
def bisection(a, b, tol=1e-6, max_iter=100): 
    fa, fb = f(a), f(b) 
    if fa * fb > 0: 
        raise ValueError("f(a) dan f(b) harus berlawanan tanda. Pilih interval lain.") 
    history = [] 
    start = pc() 
    for i in range(1, max_iter+1): 
        c = (a + b) / 2.0 
        fc = f(c) 
        history.append((i, a, b, c, fc)) 
        print(f"Iter {i:2d}: a={a:.8f}, b={b:.8f}, c={c:.8f}, f(c)={fc :.8e}") 
        if abs(fc) < tol or (b - a)/2.0 < tol: 
            end = pc() 
            print(f"\nAkar diperkirakan di x = {c:.12f}") 
            print(f"f(c) = {fc:.12e}") 
            print(f"Iterasi = {i}, waktu = {(end-start):.6f} s") 
            return c, history 
        if fa * fc < 0: 
            b = c 
            fb = fc 
        else: 
            a = c 
            fa = fc 
    end = pc() 
    print("\nMetode tidak konvergen dalam batas iterasi.") 
    return c, history
 
# Menjalankan metode pada interval [1, 2] 
akar, hist = bisection(1, 2, tol=1e-6, max_iter=100) 
 
# Visualisasi fungsi dan titik-titik mid tiap iterasi 
x = np.linspace(0.5, 2.5, 400)
y = f(x)

mid_points = [h[3] for h in hist]
f_mid = [f(c) for c in mid_points]
plt.figure(figsize=(8, 5))
plt.axhline(0, color='black', linewidth=1)           
plt.plot(x, y, color ='grey',label='f(x) = x³ + x² - 3x - 3')      
plt.scatter(mid_points, f_mid, color='plum', label='Titik mid tiap iterasi')
plt.scatter(akar, f(akar), color='skyblue', s=60, label=f'Akar ≈ {akar:.6f}')
plt.title('Visualisasi Metode Bisection')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

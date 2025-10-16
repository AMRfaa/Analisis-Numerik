#Menyelesaikan Persamaan Non Linear x^3+x^2-3x-3 dengan Metode Secant
 
# Mengimport library yang digunakan
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter as pc

# Mendefinisikan fungsi 
def f(x): 
    return x**3 + x**2 - 3*x - 3 

# Metode Secant 
def secant(x0, x1, tol=1e-6, max_iter=100): 
    print("Iterasi\t   x0\t\t   x1\t\t   x2\t\tf(x2)") 
    nilai_x = []
    start = pc()  
    for i in range(max_iter): 
        f0 = f(x0) 
        f1 = f(x1) 
        if f1 - f0 == 0: 
            print("Error: karena pembagian dengan nol") 
            break 
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0) 
        f2 = f(x2) 
        
        print(f"{i+1}\t{x0:.6f}\t{x1:.6f}\t{x2:.6f}\t{f2:.6f}") 
        nilai_x.append(x2) 
        
        if abs(f2) < tol: 
            end = pc()  
            print(f"Akar diperkirakan di x = {x2:.12f}")
            print(f"f(x) = {f2:.12e}")
            print(f"Iterasi = {i+1}, waktu = {(end - start):.6f} s")
            return x2, nilai_x
        
        x0, x1 = x1, x2 
    print("\nMetode tidak konvergen.") 
    return None, nilai_x 

# Menjalankan metode dengan tebakan awal 
akar, nilai_x = secant(2, 3) 

# Visualisasi hasil 
x = np.linspace(0, 3, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.axhline(0, color='black', linewidth=1)
plt.plot(x, y, color='grey', label='f(x) = x³ + x² - 3x - 3')
plt.scatter(nilai_x, [f(xi) for xi in nilai_x], color='aqua', label='Hasil iterasi')
plt.scatter(akar, f(akar), color='violet', s=60, label=f'Akar ≈ {akar:.6f}')
plt.title('Visualisasi Metode Secant')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

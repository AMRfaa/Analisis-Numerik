#Menyelesaikan Persamaan Non Linear x^3+x^2-3x-3 dengan Metode Newton-Raphson 

# Mengimport library yang digunakan
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter as pc 
 
# Mendefinisikan fungsi dan turunannya 
def f(x): 
    return x**3 + x**2 - 3*x - 3 
def f_prime(x): 
    return 3*x**2 + 2*x - 3 
 
# Metode Newton-Raphson 
def newton_raphson(x0, tol=1e-6, max_iter=100): 
    print("Iterasi\t   x\t\t   f(x)") 
    nilai_x = [] 
    start = pc()    
    for i in range(max_iter): 
        fx = f(x0) 
        fpx = f_prime(x0) 

        if fpx == 0: 
            print("Turunan nol, metode berhenti.") 
            break 
         
        x1 = x0 - fx / fpx 
        print(f"{i+1}\t{x0:.6f}\t{fx:.6f}") 
        nilai_x.append(x1) 
         
        if abs(x1 - x0) < tol: 
            end = pc()                
            print(f"\nAkar diperkirakan di x = {x1:.12f}") 
            print(f"f(x) = {f(x1):.12e}") 
            print(f"Iterasi = {i+1}, waktu = {(end - start):.6f} s") 
            return x1, nilai_x
        
        x0 = x1 
     
    print("\nMetode tidak konvergen.") 
    return None, nilai_x 
 
# Menjalankan metode dengan tebakan awal 
akar, nilai_x = newton_raphson(3) 
 
# Visualisasi hasil
x = np.linspace(0, 3, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.axhline(0, color='black', linewidth=1)
plt.plot(x, y, color='grey', label='f(x) = x³ + x² - 3x - 3')
plt.scatter(nilai_x, [f(xi) for xi in nilai_x], color='lawngreen', label='Hasil iterasi')
plt.scatter(akar, f(akar), color='green', s=60, label=f'Akar ≈ {akar:.6f}')
plt.title('Visualisasi Metode Newton-Raphson')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

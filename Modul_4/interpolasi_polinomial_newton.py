import numpy as np
import matplotlib.pyplot as plt

# data titik
x  = np.array([1.0, 2.0, 3.0])
y  = np.array([3.0, 8.0, 15.0])
xp = 2.5

# fungsi interpolasi newton
def newton_interpolation(x, y, xp):
    n = len(x)
    diff = np.zeros((n,n))
    diff[:,0] = y

    # tabel selisih
    for j in range(1, n):
        for i in range(n-j):
            diff[i][j] = (diff[i+1][j-1] - diff[i][j-1]) / (x[i+j] - x[i])

    # menghitung nilai interpolasi
    result = diff[0,0]
    product = 1.0
    for i in range(1, n):
        product *= (xp - x[i-1])
        result += diff[0,i] * product

    return result

# hasil
n_value = newton_interpolation(x, y, xp)
print("Newton f(2.5) =", n_value)

# ---- Grafik ----- #
# buat titik untuk kurva interpolasi
x_plot = np.linspace(min(x), max(x), 100)
y_plot = [newton_interpolation(x, y, xi) for xi in x_plot]

plt.plot(x_plot, y_plot, label="Kurva Interpolasi Newton")
plt.scatter(x, y, color="red", label="Titik Data")
plt.scatter(xp, n_value, color="green", label=f"f({xp}) = {n_value:.2f}")

plt.title("Interpolasi Newton")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

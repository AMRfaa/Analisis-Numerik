import numpy as np
import matplotlib.pyplot as plt
# data titik
x  = np.array([10, 20, 30, 40]) # ukuran aplikasi (MB)
y  = np.array([2.5, 4, 5, 6.5]) # waktu muat (detik)

# hitung parameter regresi
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

# rumus slope (b1) dan interept (b0)
b1 = np.sum ((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
b0 = y_mean - b1 * x_mean
print("persamaan regresi: y = {:4.4f}x + {:.4f}".format(b1,b0))

# contoh prediksi (misalnya ukuran 25 MB)
x_prediction = 100
y_prediction = b0 + b1 * x_prediction
print("Prediksi waktu muat untuk ukuran 100 MB =", y_prediction)

# ---- Grafik ----- #
x_line = np.linspace(min(x), x_prediction, 200)
y_line = b0 + b1 * x_line

plt.figure(figsize=(8,5))
plt.plot(x_line, y_line, label="Garis Regresi (linear)")
plt.scatter(x, y, marker='o', label="Titik data")
plt.scatter([x_prediction], [y_prediction], marker='s', label=f"Prediksi {x_prediction:.0f} MB", zorder=5)
plt.annotate(f"{y_prediction:.2f} s", (x_prediction, y_prediction),
             textcoords="offset points", xytext=(5,5))

plt.xlabel('Ukuran aplikasi (MB)')
plt.ylabel('Waktu muat (detik)')
plt.title('Regresi Linear: Ukuran vs Waktu Muat')
plt.legend()
plt.grid(True)
plt.show()

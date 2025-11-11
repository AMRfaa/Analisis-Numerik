import numpy as np

#  x -  y +  z = 0
# 3x + 2y - 2z = 5
#  x + 3y + 3z = 4

A = np.array([[ 1, -1,  1],
              [ 3,  2, -2],
              [ 1,  3,  3]], dtype=float)
b = np.array([0, 5, 4], dtype=float)

# Tampilkan koefisien awal
print("Koefisien A:")
print(A)
print("\nSisi kanan b:")
print(b)

# Bentuk matriks augmented
augmented = np.column_stack((A, b))
print("\nMatriks augmented awal:")
print(augmented)

# leb(b) itu jumlah elemen atau indeks dlam matriks b
n = len(b)

# eliminasi 2 angka di bwah pivot
for k in range(n-1):
    # pivoting: cari baris untuk posisi k
    # k: = kolom ke-k smpai terakhir
    # k = baris ke-k
    # abs = agar nilai mutlak
    # argmax = mencari angka terbesar
    max_row = np.argmax(np.abs(augmented[k:, k])) + k
    if max_row != k:
      # menukar baris jika nilai terbesar pada baris tidak sama dengan k(0)
      # kalau ternyata baris terbesar bukan baris pertama
        augmented[[k, max_row]] = augmented[[max_row, k]]
        print(f"\nTukar baris {k} dengan baris {max_row} (pivoting):")
        print(augmented)

    # k+1 = 0+1 = 1
    # (1,3) = 1 sampai 2
    # i = indeks dari 1 samai 2
    for i in range(k+1, n):
        # jika matriks baris k, kolom k sama denagn 0 maka program diberi info error
        if augmented[k, k] == 0:
            raise ValueError("Pivot nol, perlu penanganan lebih lanjut.")
        # membuat faktor dari angka di bawah pivot
        # mtariks augmented di baris ke-i(1) dan kolom k(0)
        factor = augmented[i, k] / augmented[k, k]

        # Operasi baris: Ri = Ri - factor * Rk
        augmented[i, k:] = augmented[i, k:] - factor * augmented[k, k:]
        print(f"\nEliminasi: kurangi {factor:.4f} * baris {k} dari baris {i}:")
        print(augmented)

# Augmented bentuk segitiga atas
print("\nMatriks augmented setelah forward elimination (segitiga atas):")
print(augmented)

# substitusi
# x membuat array dengn n = 3 berarti membuat 0 sebnyak 3 didalam array
x = np.zeros(n)
# perulangan dari n=3 dikurang 1 sampai 0 karna -1 dibawahny range(2,1,0)
for i in range(n-1, -1, -1):
    # pivot baris 0, kolom 0 (3)= 0
    # pivot baris 1, kolom 1 (2.333)= 0
    # pivot baris 2, kolom 2 (4.285)= 0
    if augmented[i, i] == 0:
        raise ValueError("Diagonal nol saat substitusi.")

    # x(i=2,1,0) > baris ke 2, baris ke 1, baris ke 0
    # matriks baris 2 kolom -1 = sisi kanan atau indeks elemen terakhir=(4)
    # z (i=2), y (i=1), x (i-0)


    x[i] = (augmented[i, -1] - np.dot(augmented[i, i+1:n], x[i+1:n])) / augmented[i, i]
    # x[2] = (augmented[2, -1] - np.dot(augmented[2, 3:3], x[3:3])) / augmented[2, 2]
    # augmented[2,-1] = 0 → sisi kanan
    # augmented[2, 3:3] = [] → tidak ada elemen di kanan diagonal
    # x[3:3] = [] → tidak ada variabel yang sudah dihitung
    # np.dot([],[]) = 0
    print(f"\nHitung x[{i}]: {x[i]:.6f}")

print("\nSolusi (x, y, z):")
print(x)

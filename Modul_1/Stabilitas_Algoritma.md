# Algoritma Penjumlahan

## Algoritma A

  '''bash
  •	Hasil Analitik:
  100000 + (0,00001 + 0,00001 + … + 0,00001 sampain yang ke 100.000 kali) = 100001
  •	Hasil Numerik:
  100000 + 0,00001 + 0,00001 + … + 0,00001 sampain yang ke 100.000 kali = 100001,00000033854
  •	Galat : 100001 - 100001,00000033854 = 0,00000033854
  '''

## Algoritma B

  '''bash  
  •	Hasil Analitik:
  (0,00001 + 0,00001 + … + 0,00001 sampain yang ke 100.000 kali) + 100000 = 100001
  •	Hasil Numerik:
  (0,00001 + 0,00001 + … + 0,00001 sampain yang ke 100.000 kali) + 100000 = 100001
  •	Galat : 100001 - 100001 = 0
  '''

		Jadi dilihat dari hasil kedua algoritma A dan B bahwa hasil dari masing-masing algoritma tidak sama persis. Kemudian dilihat dari galat algoritma A dan B terdapat perbedaan galat dimana algoritma A memiliki galat sebesar 0,00000033854 sedangkan algoritma B tidak memiliki galat.
		Perbedaan algoritma A dan B muncul karena komputer menggunakan presisi terbatas atau disebut floating point yaitu keterbatasan dalam menyimpan angka. Nah perbedaannya juga dapat dilihat pada algoritma A, penjumlahan dihitung dengan cara menambahkan bilangan besar baru kemudian bilangan kecil secara berulang sebnyak 100.000 kali dimana angka kecil tersebut sering diabaikan oleh komputer, sehingga kesalahan pembuklatan menumpuk dan memperbesar galat, ini dapat menunjukan bahwa algoritma A tidak stabil. Sedangkan algoritma B, penjumlahan dihitung dengan cara menjumlahkan bilangan terkecil dahulu baru ditambahkan dengan bilangan besar, sehingga hasilnya lebih mendekati nilai sebenarnya, ini dapat menunjukan bahwa algoritma B stabil.


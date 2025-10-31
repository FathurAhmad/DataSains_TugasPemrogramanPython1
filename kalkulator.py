import re

raw_numbers = input("Masukkan daftar angka (pisahkan dengan koma): ")
numbers_string = re.split(r'\s*,\s*', raw_numbers.strip())
numbers_float = [float(num) for num in numbers_string]

average = sum(list(numbers_float)) / len(numbers_float)
print("Rata-rata: ", average)

max_number = max(list(numbers_float))
print("Maksimum: ", max_number)

min_number = min(list(numbers_float))
print("Minimum: ", min_number)

jumlah_angka = len(numbers_float)
print("Jumlah angka: ", jumlah_angka)

angka_genap = [int(num) for num in numbers_float if int(num) % 2 == 0]
print("Angka genap: ", len(angka_genap))

angka_ganjil = [int(num) for num in numbers_float if int(num) % 2 != 0]
print("Angka ganjil: ", len(angka_ganjil))
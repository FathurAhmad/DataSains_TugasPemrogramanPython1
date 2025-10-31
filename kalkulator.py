import re

raw_numbers = input("Masukkan daftar angka (pisahkan dengan koma): ")
numbers_string = re.split(r'\s*,\s*', raw_numbers.strip())
numbers_int = [int(num) for num in numbers_string]

average = sum(list(numbers_int)) / len(numbers_int)
print("Rata-rata: ", average)

max_number = max(list(numbers_int))
print("Maksimum: ", max_number)

min_number = min(list(numbers_int))
print("Minimum: ", min_number)

jumlah_angka = len(numbers_int)
print("Jumlah angka: ", jumlah_angka)

angka_genap = [int(num) for num in numbers_int if int(num) % 2 == 0]
print("Angka genap: ", len(angka_genap))

angka_ganjil = [int(num) for num in numbers_int if int(num) % 2 != 0]
print("Angka ganjil: ", len(angka_ganjil))
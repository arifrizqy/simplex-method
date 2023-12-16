import numpy as np
import re

# String yang mengandung ekspresi aljabar
input_string = "12x_1 + 3x_2 - 4x_3 = 30"

# Mencari dan mengekstrak angka dari string menggunakan regex
numbers = re.findall(r'[-+]?\d+', input_string)

# Mengubah angka-angka yang ditemukan menjadi list of integers
numbers = np.array([int(num) for num in numbers])

# Menampilkan angka-angka yang berhasil diekstrak
print("Angka yang diekstrak:", numbers)

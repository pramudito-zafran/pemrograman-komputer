# Tes conditional lagi


# 1. Tes kesetaraan dan ketidaksetaraan dengan string
makanan = 'Sate'
print("Apakah makanan == 'Sate'? Harusnya True.")
print(makanan == 'Sate')

print("\nApakah makanan != 'Sate'? Harusnya False.")
print(makanan != 'Sate')


# 2. Tes menggunakan metode lower()
nama_pengguna = 'BudiUtomo'
print("\nApakah nama_pengguna.lower() == 'budiutomo'? Harusnya True.")
print(nama_pengguna.lower() == 'budiutomo')

print("\nApakah nama_pengguna.lower() == 'BudiUtomo'? Harusnya False.")
print(nama_pengguna.lower() == 'BudiUtomo')


# 3. Tes numerik (kesetaraan, ketidaksetaraan, >, <, >=, <=)
nilai = 80

print("\nApakah nilai == 80? Harusnya True.")
print(nilai == 80)

print("\nApakah nilai != 80? Harusnya False.")
print(nilai != 80)

print("\nApakah nilai > 75? Harusnya True.")
print(nilai > 75)

print("\nApakah nilai < 75? Harusnya False.")
print(nilai < 75)

print("\nApakah nilai >= 80? Harusnya True.")
print(nilai >= 80)

print("\nApakah nilai <= 50? Harusnya False.")
print(nilai <= 50)


# 4. Tes menggunakan kata kunci 'and' dan 'or'
umur_0 = 22
umur_1 = 17

print("\nApakah umur_0 >= 21 and umur_1 >= 21? Harusnya False.")
print(umur_0 >= 21 and umur_1 >= 21)

print("\nApakah umur_0 >= 21 or umur_1 >= 21? Harusnya True.")
print(umur_0 >= 21 or umur_1 >= 21)


# 5. Tes apakah suatu item ada di dalam list
menu_restoran = ['nasi goreng', 'mie ayam', 'bakso']

print("\nApakah 'mie ayam' ada di dalam menu_restoran? Harusnya True.")
print('mie ayam' in menu_restoran)

print("\nApakah 'soto' ada di dalam menu_restoran? Harusnya False.")
print('soto' in menu_restoran)


# 6. Tes apakah suatu item tidak ada di dalam list
pengguna_diblokir = ['andi', 'siti', 'dewi']

print("\nApakah 'budi' tidak ada di dalam pengguna_diblokir? Harusnya True.")
print('budi' not in pengguna_diblokir)

print("\nApakah 'siti' tidak ada di dalam pengguna_diblokir? Harusnya False.")
print('siti' not in pengguna_diblokir)

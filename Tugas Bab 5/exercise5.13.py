print("===Kalkulator Pembagian Sederhana===")
print("Masukkan 'q' kapan saja untuk keluar.\n")

while True:
    # Mengambil input angka pertama dari pengguna
    angka_pertama = input("Masukkan angka pertama: ")
    if angka_pertama.lower() == 'q':
        break
        
    # Mengambil input angka kedua dari pengguna
    angka_kedua = input("Masukkan angka kedua: ")
    if angka_kedua.lower() == 'q':
        break

    # Menggunakan try-except untuk mencegah program crash akibat error
    try:
        hasil = float(angka_pertama) / float(angka_kedua)
    except ZeroDivisionError:
        # Menangani kesalahan jika pembagi adalah angka 0
        print("Error: Anda tidak bisa membagi angka dengan nol (0)!\n")
    except ValueError:
        # Menangani kesalahan jika pengguna memasukkan huruf/teks bukan angka
        print("Error: Pastikan Anda memasukkan angka yang valid.\n")
    else:
        # Menampilkan hasil jika tidak ada error
        print(f"Hasil: {angka_pertama} / {angka_kedua} = {hasil}\n")

print("Program selesai")

prompt = "\nMasukkan topping pizza yang Anda inginkan (atau ketik 'quit' untuk selesai): "

while True:
    topping = input(prompt)
    # Memeriksa apakah pengguna ingin keluar dari program
    if topping.strip().lower() == 'quit':
        break
    # Menampilkan pesan konfirmasi topping
    print(f"Saya akan menambahkan {topping} ke pizza Anda!")

prompt = "\nSilakan masukkan usia Anda (atau ketik 'quit' untuk keluar): "

while True:
    usia = input(prompt)
    
    # Memeriksa apakah pengguna ingin keluar dari loop
    if usia.lower().strip() == 'quit':
        break
        
    # Mengubah input menjadi integer untuk mengevaluasi usia
    age = int(usia)
    
    # Menentukan harga tiket berdasarkan kelompok usia
    if age < 3:
        print("Tiket film Anda gratis!")
    elif age <= 12:
        print("Harga tiket film Anda adalah $10.")
    else:
        print("Harga tiket film Anda adalah $15.")

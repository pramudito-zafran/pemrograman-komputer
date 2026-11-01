# Versi 1
prompt = "\nSilakan masukkan umur Anda (atau ketik 'quit' untuk selesai): "
umur = ""

while umur != 'quit':
    umur = input(prompt)
    
    if umur != 'quit':
        # Mengubah input menjadi angka untuk pengecekan harga
        umur_angka = int(umur)
        
        if umur_angka < 3:
            print("Tiket Anda gratis!")
        elif umur_angka <= 12:
            print("Harga tiket Anda adalah $10.")
        else:
            print("Harga tiket Anda adalah $15.")


# Versi 2
prompt = "\nSilakan masukkan umur Anda (atau ketik 'quit' untuk selesai): "
active = True

while active:
    umur = input(prompt)
    
    if umur == 'quit':
        active = False
    else:
        umur_angka = int(umur)
        
        if umur_angka < 3:
            print("Tiket Anda gratis!")
        elif umur_angka <= 12:
            print("Harga tiket Anda adalah $10.")
        else:
            print("Harga tiket Anda adalah $15.")



#Versi 3
prompt = "\nSilakan masukkan umur Anda (atau ketik 'quit' untuk selesai): "

while True:
    umur = input(prompt)
    
    if umur == 'quit':
        break
        
    umur_angka = int(umur)
    if umur_angka < 3:
        print("Tiket Anda gratis!")
    elif umur_angka <= 12:
        print("Harga tiket Anda adalah $10.")
    else:
        print("Harga tiket Anda adalah $15.")

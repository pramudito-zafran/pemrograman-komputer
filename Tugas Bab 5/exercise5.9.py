nama_nama = []

if nama_nama:
    for nama in nama_nama:
        if nama == 'admin':
            print("Halo admin, apakah kamu mau melihat laporan mengenai status saat ini?")
        else:
            print(f"Halo {nama}, terimakasih sudah masuk lagi!")
else:
    print("Kita harus mencari pengguna!")
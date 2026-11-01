# Inisialisasi dictionary kosong untuk menyimpan hasil jajak pendapat (nama: destinasi)
responses = {}

# Set flag aktif untuk menunjukkan bahwa polling sedang berjalan
polling_active = True

while polling_active:
    # Meminta input nama dan destinasi liburan impian pengguna
    name = input("\nSiapa nama Anda? ")
    destination = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")
    
    # Menyimpan jawaban ke dalam dictionary
    responses[name] = destination
    
    # Memeriksa apakah ada orang lain yang ingin mengisi jajak pendapat
    repeat = input("Apakah ada orang lain yang ingin menjawab? (ya/tidak) ")
    if repeat.strip().lower() == 'tidak':
        polling_active = False

# Jawaban selesai, cetak hasilnya
print("\n====Hasil Jawaban====")
for name, destination in responses.items():
    print(f"{name.title()} ingin sekali mengunjungi {destination.title()}.")

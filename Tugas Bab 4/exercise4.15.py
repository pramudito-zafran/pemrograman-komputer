# Memperbaiki code di exercise4.13.py dengan menambah comment agar pembaca tau maksud dari setiap code
# Menu awal restoran buffet dalam bentuk tuple
menu_makanan = ('sate', 'soto', 'sayur', 'salmon', 'sosis') 

print("Silahkan memilih makanan yang ada di menu:")
for makanan in menu_makanan:
    print(f"- {makanan}")

# Kode di bawah sengaja dimatikan untuk membuktikan tuple tidak bisa diubah (immutable)
# menu_makanan[0] = 'bakso'  # Menghasilkan TypeError: 'tuple' object does not support item assignment

# Restoran mengubah menunya dengan menulis ulang tuple baru
menu_makanan = ('sate', 'soto', 'sushi', 'sup', 'sarden')

print("\nAda menu baru.")
print("Silahkan memilih makanan yang ada di menu:")
for makanan in menu_makanan:
    print(f"- {makanan}")

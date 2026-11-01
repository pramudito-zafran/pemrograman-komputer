# Program dasar: Menyimpan informasi hewan peliharaan
peliharaan = {
    'jenis': 'kucing',
    'pemilik': 'budi',
}

print(f"Ini adalah {peliharaan['jenis']} milik {peliharaan['pemilik'].title()}.")


# "Program yang sudah diperluas"

# 1. Menggunakan list dan di dalamnya ada dictionary
peliharaan_peliharaan = [
    {
        'nama': 'kiko',
        'jenis': 'kucing',
        'pemilik': 'budi',
        'umur': 3,  # Menambahkan key baru
        'makanan_favorit': 'ikan tuna'  # Menambahkan key baru
    },
    {
        'nama': 'bruno',
        'jenis': 'anjing',
        'pemilik': 'siti',
        'umur': 5,
        'makanan_favorit': 'daging sapi'
    },
    {
        'nama': 'goldie',
        'jenis': 'ikan mas',
        'pemilik': 'andi',
        'umur': 1,
        'makanan_favorit': 'pelet'
    }
]

# 2. Membuat format output yang rapi
print("="*40)
print("     DAFTAR KLINIK HEWAN PELIHARAAN     ")
print("="*40)

for peliharaan in peliharaan_peliharaan:
    print(f"Nama Hewan : {peliharaan['nama'].title()}")
    print(f"Jenis      : {peliharaan['jenis'].title()}")
    print(f"Pemilik    : {peliharaan['pemilik'].title()}")
    print(f"Umur       : {peliharaan['umur']} tahun")
    print(f"Makanan    : Sangat suka {peliharaan['makanan_favorit']}")
    print("-" * 40)

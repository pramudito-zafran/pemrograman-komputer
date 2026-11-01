# Dictionary untuk peliharaan yang berbeda-beda
peliharaan_1 = {
    'jenis': 'anjing',
    'pemilik': 'mamang'
}

peliharaan_2 = {
    'jenis': 'kucing',
    'pemilik': 'roman'
}

peliharaan_3 = {
    'jenis': 'merpati',
    'pemilik': 'pennywise'
}

# Menyimpan dictionary di atas ke dalam list
peliharaan = [peliharaan_1, peliharaan_2, peliharaan_3]

# Loop untuk masing-masing peliharaan
for peliharaan in peliharaan:
    print(f"\nYang kuketahui mengenai peliharaan ini:")
    print(f"  Jenis peliharaan: {peliharaan['jenis'].title()}")
    print(f"  Nama pemilik:     {peliharaan['pemilik'].title()}")

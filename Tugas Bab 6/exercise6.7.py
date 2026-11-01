# Membuat tiga dictionary untuk orang-orang yang berbeda
orang_1 = {
    'nama_pertama': 'aan',
    'nama_terakhir': 'ghani',
    'umur': 43,
    'kota': 'surabaya',
}

orang_2 = {
    'nama_pertama': 'jane',
    'nama_terakhir': 'siti',
    'umur': 28,
    'kota': 'malang',
}

orang_3 = {
    'nama_pertama': 'billie',
    'nama_terakhir': 'yanti',
    'umur': 35,
    'kota': 'ngawi',
}

# Menyimpan dictionary di list orang_orang
orang_orang = [orang_1, orang_2, orang_3]

# Loop untuk masing-masing orang
for orang in orang_orang:
    pertama = f"{orang['nama_pertama'].title()} {orang['nama_terakhir'].title()}"
    umur = orang['umur']
    kota = orang['kota'].title()
    
    print(f"\npertama: {pertama}")
    print(f"umur: {umur}")
    print(f"kota: {kota}")

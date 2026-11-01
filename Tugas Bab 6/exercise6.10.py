# Membuat dictionary dengan nama sebagai key dan list angka favorit sebagai value
angka_favorit = {
    'aan': [2, 4],
    'riski': [4, 9],
    'dappa': [5, 11],
    'dito': [5, 111],
    'dhino': [7, 98] 
}

# Melakukan perulangan menggunakan .items() untuk mengambil nama dan list angkanya
for nama, favorit in angka_favorit.items():
    print(f"\nAngka favorit {nama.title()} adalah:")
    for angka in favorit:
        print(f"- {angka}")

# Membuat glosarium menggunakan dictionary 
glosarium = {
    'variable': 'Sebuah nama atau label yang merujuk pada suatu nilai yang disimpan di dalam memori komputer.',
    'string': 'Serangkaian karakter atau teks yang diapit oleh tanda kutip tunggal atau ganda.',
    'list': 'Kumpulan item atau data yang disusun dalam urutan tertentu dan bersifat dinamis (bisa diubah).',
    'loop': 'Struktur pemrograman yang mengulangi serangkaian instruksi sampai kondisi tertentu terpenuhi.',
    'dictionary': 'Kumpulan pasangan kunci-nilai (key-value) di mana setiap kunci terhubung dengan nilai tertentu.'
}

# Mencetak setiap kata dan artinya dengan format yang rapi
for kata, arti in glosarium.items():
    print(f"{kata.title()}:")
    print(f"{arti}\n")


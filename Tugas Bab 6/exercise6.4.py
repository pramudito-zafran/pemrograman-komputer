glossary = {
    # Dari latihan 6-3
    'variable': 'Sebuah nama atau label yang merujuk pada suatu nilai yang disimpan di dalam memori komputer.',
    'string': 'Serangkaian karakter atau teks yang diapit oleh tanda kutip tunggal atau ganda.',
    'list': 'Kumpulan item atau data yang disusun dalam urutan tertentu dan bersifat dinamis (bisa diubah).',
    'loop': 'Struktur pemrograman yang mengulangi serangkaian instruksi sampai kondisi tertentu terpenuhi.',
    'dictionary': 'Kumpulan pasangan kunci-nilai (key-value) di mana setiap kunci terhubung dengan nilai tertentu.',
    
    # Lima istilah Python tambahan untuk Latihan 6-4
    'key': 'Item pertama dalam pasangan key-value pada sebuah dictionary.',
    'value': 'Item yang dikaitkan dengan key tertentu dalam dictionary.',
    'conditional test': 'Ekspresi logis yang mengevaluasi nilai menjadi True atau False.',
    'float': 'Tipe data numerik untuk angka yang memiliki titik desimal.',
    'comment': 'Catatan di dalam kode sumber yang diabaikan oleh interpreter Python.'
}

# Melakukan perulangan (loop) secara dinamis untuk mengambil key dan value
for kata, arti in glossary.items():
    print(f"\n{kata.title()}:")
    print(f"  {arti}")

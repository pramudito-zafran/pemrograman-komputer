from pathlib import Path

# Daftar files yang akan dibaca
filenames = ['Tugas Bab 10/exercise10.8/cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    print(f"\nMembaca {filename}")
    
    try:
        # Mencoba membaca seluruh isi berkas teks
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Menampilkan pesan jika files tidak ada
        print(f"Maaf, berkas '{filename}' tidak ditemukan. Silakan periksa lokasinya.")
    else:
        # Menampilkan isi berkas jika berhasil dibaca tanpa error
        print(contents.strip())

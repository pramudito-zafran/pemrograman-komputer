from pathlib import Path
import json

# Menentukan path file tempat data disimpan
path = Path('Tugas Bab 10/exercise10.11/angka_favorit.json')

if path.exists():
    # Jika file sudah ada, baca data dan tampilkan
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"Nomor favorit Anda adalah {fav_number}.")
else:
    # Jika file belum ada, minta input dan simpan data
    fav_number = input("Berapa nomor favorit Anda? ")
    contents = json.dumps(fav_number)
    path.write_text(contents)
   

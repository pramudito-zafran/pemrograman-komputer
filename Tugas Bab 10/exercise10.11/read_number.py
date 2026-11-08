from pathlib import Path
import json

path = Path('Tugas Bab 10/exercise10.11/angka_favorit.json')
isi = path.read_text()
angka_favorit = json.loads(isi)
print(angka_favorit)

from pathlib import Path
import json

angka_favorit = input('Angka kesukaanmu apa? ')
path = Path('Tugas Bab 10/exercise10.11/angka_favorit.json')
isi = json.dumps(angka_favorit)
path.write_text(isi)


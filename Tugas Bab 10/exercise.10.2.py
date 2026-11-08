from pathlib import Path
path = Path('Tugas Bab 10/exercise10.1/belajar_python.txt')
isi = path.read_text().replace('Python', 'C').title()

baris_baris = isi.splitlines()

for baris in baris_baris:
    print(baris)
    
from pathlib import Path
path = Path('Tugas Bab 10/exercise10.1/belajar_python.txt')
isi = path.read_text().replace('Python', 'C').title()

for baris in isi.splitlines():
    print(baris)

pi_string = ''
for baris in isi.splitlines():
    pi_string += baris

print(pi_string)
print(len(pi_string))
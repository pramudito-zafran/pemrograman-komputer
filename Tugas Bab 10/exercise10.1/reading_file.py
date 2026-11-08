from pathlib import Path

path = Path('Tugas Bab 10/exercise10.1/belajar_python.txt')


# Membaca seluruh file
print('==Membaca Seluruh File==')
contents = path.read_text().title()
print(contents)


# Membaca baris per baris
print("\n==Membaca Baris Per Baris===")
lines = contents.splitlines()

for line in lines:
    print(line)
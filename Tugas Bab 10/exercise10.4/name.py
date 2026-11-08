from pathlib import Path
path = Path('Tugas Bab 10/exercise10.4/guest.txt')

nama = input('Siapa namamu? ').title().strip()
file_guest = path.write_text(nama)


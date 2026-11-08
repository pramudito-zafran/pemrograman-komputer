from pathlib import Path

filenames = ['cats.txt', 'Tugas Bab 10/exercise10.8/dogs.txt']

for filename in filenames:
    path = Path(filename)
    try:
        # Membaca konten file menggunakan path
        contents = path.read_text(encoding='utf-8')
        print(contents)
    except FileNotFoundError:
        pass

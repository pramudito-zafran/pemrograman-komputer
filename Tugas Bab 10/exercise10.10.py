from pathlib import Path

def count_words(path):
    """Menghitung perkiraan jumlah kata dalam sebuah berkas."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Maaf, file {path} tidak ada.")
    else:
        # Menghitung perkiraan jumlah kata di dalam berkas:
        words = contents.split()
        num_words = len(words)
        print(f"file {path} punya {num_words} kata.")

# Daftar berkas teks yang ingin dianalisis
filenames = ['cats.txt', 'Tugas Bab 10/exercise10.8/dogs.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)

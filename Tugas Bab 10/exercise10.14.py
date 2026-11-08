import json
from pathlib import Path

def get_stored_username(path):
    """Mengambil nama pengguna yang tersimpan jika tersedia."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    return None

def get_new_username(path):
    """Meminta nama pengguna baru dan menyimpannya."""
    username = input("Siapa nama Anda? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Menyapa pengguna, memverifikasi identitas terlebih dahulu."""
    path = Path("username.json")
    username = get_stored_username(path)
    
    if username:
        # Menanyakan apakah ini pengguna yang benar
        correct = input(f"Apakah Anda adalah '{username}'? (ya/tidak): ")
        if correct.strip().lower() == 'ya':
            print(f"Selamat datang kembali, {username}!")
            return
            
    # Jika tidak ada user tersimpan atau pengguna saat ini menjawab 'tidak'
    username = get_new_username(path)
    print(f"Kami akan mengingat Anda saat Anda kembali, {username}!")

# Menjalankan program utama
greet_user()

import json
from pathlib import Path

path = Path("Tugas Bab 10/exercise10.13/.user_profile.json")

if path.exists():
    # Membaca dictionary dari file JSON
    contents = path.read_text()
    user_dict = json.loads(contents)
    
    # Mencetak ringkasan informasi yang diingat
    print("\n=== Berikut data tentang Anda ===")
    print(f"Nama Pengguna : {user_dict['username']}")
    print(f"Usia          : {user_dict['age']} tahun")
    print(f"Kota Asal     : {user_dict['location']}")
else:
    # Meminta tiga informasi dari pengguna
    username = input("Namanya siapa bang? ")
    age = input("Usianya berapa bang? ")
    location = input("Tinggal di mana bang? ")
    
    # Menyusun data ke dalam dictionary
    user_dict = {
        "username": username,
        "age": age,
        "location": location
    }
    
    # Menyimpan dictionary ke file
    contents = json.dumps(user_dict)
    path.write_text(contents)
   
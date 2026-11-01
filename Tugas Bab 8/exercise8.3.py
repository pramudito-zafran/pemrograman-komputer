def make_shirt(size, message):
    """Menampilkan ukuran dan pesan yang dicetak pada kaus."""
    print(f"Membuat kaus ukuran {size} dengan pesan: '{message}'.")

# 1. Memanggil fungsi menggunakan positional arguments (argumen posisi)
make_shirt("L", "Semangat Ngoding!")

# 2. Memanggil fungsi menggunakan keyword arguments (argumen kata kunci)
make_shirt(message="Hello World", size="M")

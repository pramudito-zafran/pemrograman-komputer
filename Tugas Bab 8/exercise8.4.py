def make_shirt(size="L", message="I love Python"):
    """Menampilkan ukuran dan pesan kaus dengan nilai default."""
    print(f"Membuat kaus ukuran {size} dengan pesan: '{message}'.")

# 1. Membuat kaus ukuran besar L dengan pesan 
make_shirt()

# 2. Membuat kaus ukuran sedang M dengan pesan 
make_shirt(size="M")

# 3. Membuat kaus ukuran bebas dengan pesan yang berbeda
make_shirt(size="S", message="Python menyenangkan ya")

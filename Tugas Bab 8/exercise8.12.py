def make_sandwich(*items):
    """Menampilkan ringkasan sandwich yang sedang dipesan."""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for item in items:
        print(f"- {item}")

# Memanggil fungsi tiga kali dengan jumlah argumen yang berbeda
make_sandwich('daging kalkun', 'keju swiss', 'selada', 'tomat')
make_sandwich('daging sapi asap', 'keju cheddar')
make_sandwich('selai kacang', 'jeli')

"""Modul contoh yang telah memenuhi standar penataan gaya PEP 8."""


def sapa_pengguna(nama_pengguna):
    """Menampilkan sapaan sederhana kepada pengguna."""
    print(f"Halo, {nama_pengguna.title()}!")


def buat_baju(ukuran, teks_cetak='I love Python'):
    """Merangkum ukuran baju dan tulisan yang akan dicetak."""
    print(f"\nMembuat baju ukuran: {ukuran.upper()}")
    print(f"Teks cetakan: '{teks_cetak}'")


# --- Area Eksekusi Utama ---
sapa_pengguna(nama_pengguna='budi')

# Memanggil fungsi dengan argumen kata kunci tanpa spasi di sekitar tanda '='
buat_baju(ukuran='m')
buat_baju(ukuran='xl', teks_cetak='Semangat belajarnya bro')

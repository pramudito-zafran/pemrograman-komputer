# 1. Membuat daftar pesanan awal dengan 'pastrami' minimal muncul 3 kali
sandwich_orders = [
    'pastrami', 'tuna', 'turkey', 'pastrami', 
    'roast beef', 'pastrami', 'chicken bacon ranch'
]
finished_sandwiches = []

# 2. Menampilkan pesan pengumuman di awal program bahwa pastrami habis
print("Maaf, kedai deli kami kehabisan daging pastrami hari ini!\n")

# 3. Menggunakan while loop untuk menghapus semua kemunculan 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 4. Memproses sisa pesanan sandwich yang ada
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

# 5. Menampilkan semua sandwich yang berhasil dibuat
print("\n====Semua Sandwich yang Selesai Dibuat====")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")

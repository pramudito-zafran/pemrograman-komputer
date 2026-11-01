# Mulai dengan daftar pesanan sandwich 
sandwich_orders = [
    'tuna', 'pastrami', 'turkey', 'pastrami', 
    'grilled cheese', 'pastrami', 'roast beef'
]

# Daftar kosong untuk menampung sandwich yang sudah selesai dibuat
finished_sandwiches = []

# Tampilkan pesan bahwa deli kehabisan pastrami
print("Maaf, deli kami kehabisan daging pastrami hari ini.\n")

# Gunakan while loop untuk menghapus semua kemunculan 'pastrami' dari sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop untuk membuat sandwich yang tersisa
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    
    print(f"Saya telah membuat sandwich {current_sandwich} Anda.")
    finished_sandwiches.append(current_sandwich)

# Cetak ringkasan semua sandwich yang berhasil dibuat
print("\nBerikut daftar sandwich yang telah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")

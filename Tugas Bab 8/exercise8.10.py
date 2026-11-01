def send_messages(messages, sent_messages):
    """Mencetak setiap pesan teks dan memindahkannya ke daftar sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

# Menginisialisasi daftar awal dan daftar pesan terkirim
unsent_messages = ["Halo apa kabar?", "Bagaimana belajarnya?", "Jangan lupa latihan Python!", "Sampai jumpa nanti!"]
sent_messages = []

# Memanggil fungsi untuk mengirim dan memindahkan pesan
send_messages(unsent_messages, sent_messages)

# Mencetak kedua daftar untuk memastikan pesan telah berpindah dengan benar
print("\n====Verifikasi Akhir Daftar====")
print(f"Daftar asli (seharusnya kosong): {unsent_messages}")
print(f"Daftar pesan terkirim (seharusnya terisi semua): {sent_messages}")

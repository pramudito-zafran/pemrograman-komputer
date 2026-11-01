def send_messages(messages, sent_messages):
    """Mencetak setiap pesan teks dan memindahkannya ke daftar sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

# Menginisialisasi daftar asli
original_messages = ["Halo apa kabar?", "Bagaimana belajarnya?", "Jangan lupa latihan Python!", "Sampai jumpa nanti!"]
sent_messages_archive = []

# Memanggil fungsi dengan salinan daftar asli menggunakan notasi slice [:]
send_messages(original_messages[:], sent_messages_archive)

# Mencetak kedua daftar untuk membuktikan daftar asli tetap mempertahankan isinya
print("\n--- Verifikasi Akhir Daftar ---")
print(f"Daftar asli (tetap utuh): {original_messages}")
print(f"Daftar pesan terkirim (arsip): {sent_messages_archive}")

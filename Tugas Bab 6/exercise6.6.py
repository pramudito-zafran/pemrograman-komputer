bahasa_pemrograman = {
    'aan': 'python',
    'ghani': 'c',
    'dappa': 'javascript',
    'emka': 'python',
}

# 1. Buat list orang yang harus mengikuti polling
orangPolling = ['emka', 'fikri', 'bambang', 'ghani', 'ariq', 'akbar']

# 2. Loop dari daftar orang tersebut
for orang in orangPolling:
    # Periksa apakah nama orang tersebut ada di dalam key dictionary!
    if orang in bahasa_pemrograman:
        print(f"Terima kasih, {orang.title()}, karena telah mengisi polling kami!")
    else:
        print(f"Halo {orang.title()}, kami mengundang Anda untuk mengisi polling bahasa favorit kami.")

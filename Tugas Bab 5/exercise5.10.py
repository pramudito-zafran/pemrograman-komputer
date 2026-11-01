pengguna_lama = ['maya', 'adit', 'sopo', 'Jarwo', 'Denis']
pengguna_baru = ['MAYA', 'SOPO', 'Radit', 'oleh', 'babeh']

pengguna_lama_lower = [pengguna.lower() for pengguna in pengguna_lama]

for namaBaru in pengguna_baru:
    if namaBaru.lower() in pengguna_lama_lower:
        print(f"Sorry {namaBaru}, nama tersebut telah diambil oleh player lain.")
    else:
        print(f"Mantap, nama {namaBaru} masih tersedia.")
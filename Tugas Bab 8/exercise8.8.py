def make_album(artist_name, album_title, number_of_songs=None):
    """Membangun kamus dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist_name,
        'title': album_title,
    }
    if number_of_songs is not None:
        album['songs'] = number_of_songs
    return album

# Loop 'while' untuk mengizinkan pengguna memasukkan data secara interaktif
while True:
    print("\nSilakan masukkan detail album (atau ketik 'q' untuk keluar):")
    
    artist = input("Nama musisi/artis: ")
    if artist.lower() == 'q':
        break
        
    title = input("Judul album: ")
    if title.lower() == 'q':
        break
    
    # Memanggil fungsi make_album dengan input dari pengguna dan mencetaknya
    user_album = make_album(artist, title)
    print(f"Kamus Album yang Dibuat: {user_album}")

print("\nProgram ditutup. Selesai")

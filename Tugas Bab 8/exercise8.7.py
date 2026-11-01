def make_album(artist_name, album_title, number_of_songs=None):
    """Membangun dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist_name,
        'title': album_title,
    }
    # Menambahkan jumlah lagu ke dalam dictionary hanya jika nilainya diberikan
    if number_of_songs is not None:
        album['songs'] = number_of_songs
    return album

# Membuat tiga dictionary yang mewakili album berbeda
album1 = make_album('Pink Floyd', 'The Dark Side of the Moon')
album2 = make_album('Daft Punk', 'Discovery')
album3 = make_album('Michael Jackson', 'Thriller')

# Mencetak setiap nilai kembalian untuk memverifikasi penyimpanan data
print(album1)
print(album2)
print(album3)

# Membuat panggilan fungsi baru yang menyertakan jumlah lagu (opsional)
album_dengan_lagu = make_album('The Beatles', 'Abbey Road', number_of_songs=17)
print(album_dengan_lagu)

tempatFavorit = {
    'budi': ['jakarta', 'raja ampat', 'tokyo'],
    'siti': ['bandung', 'paris', 'surabaya'],
    'iwan': ['jogja', 'jakarta', 'gurun pasir'],
}

# Melakukan perulangan melalui dictionary
for nama, daftar_tempat in tempatFavorit.items():
    print(f"\nTiga tempat favorit {nama.title()} adalah:")
    # Melakukan loop untuk menampilkan setiap tempat di dalam list
    for tempat in daftar_tempat:
        print(f"- {tempat.title()}")

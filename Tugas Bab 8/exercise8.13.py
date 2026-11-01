def build_profile(first, last, **user_info):
    """Membuat kamus yang berisi semua informasi tentang pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Membuat profil kustom dengan nama depan, nama belakang, dan tiga pasangan kunci-nilai (key-value)
my_profile = build_profile(
    'budi', 
    'santoso', 
    bidang='ilmu komputer', 
    lokasi='jakarta', 
    hobi='fotografi'
)

print(my_profile)

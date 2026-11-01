def city_country(city, country):
    """Mengembalikan string dengan format 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"

# Memanggil fungsi dengan 3 pasangan kota-negara yang berbeda
print(city_country('ngawi', 'indonesia'))
print(city_country('jakarta', 'indonesia'))
print(city_country('tokyo', 'japan'))

def describe_city(city, country="indonesia"):
    """Menampilkan kalimat sederhana tentang kota dan negaranya."""
    print(f"{city.title()} berada di negara {country.title()}.")

# 1. Kota pertama di negara default
describe_city("jakarta")

# 2. Kota kedua di negara default
describe_city("bandung")

# 3. Kota ketiga di luar negara default
describe_city("tokyo", "jepang")

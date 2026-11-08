def city_country(city, country, population=None):
    """Return a single string of the form 'City, Country - population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

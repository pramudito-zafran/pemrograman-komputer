from city_functions2 import city_country

def test_city_country():
    """Does a simple city and country pair work?"""
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    """Can we include a population parameter?"""
    formatted_name = city_country('santiago', 'chile', population=5000000)
    assert formatted_name == 'Santiago, Chile - population 5000000'

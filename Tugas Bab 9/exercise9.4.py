class Restoran:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe(self):
        print(f'Name of the restaurant = {self.name}')
        print(f'The type of cuisine that they offered = {self.cuisine_type}')

    def open(self):
        print(f'{self.name} is opening now')

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't roll back the number of served customers!")

    def increment_number_served(self, additional_customers):
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("You can't add negative customers!")



# Buat restaurant-nya dulu
restaurant = Restoran ("The Pizza Place", "Italian")

# Print numeber awal
print(f"Initial customers served: {restaurant.number_served}")

# Ada customer
restaurant.number_served = 15
print(f"Customers served (after direct change): {restaurant.number_served}")

# Tambah customer lagi
restaurant.set_number_served(35)
print(f"Customers served (after set_number_served): {restaurant.number_served}")

# Tambah customer lagi
restaurant.increment_number_served(20)
print(f"Customers served (after increment_number_served): {restaurant.number_served}")

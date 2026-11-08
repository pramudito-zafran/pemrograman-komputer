class Restoran:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f'Name of the restaurant = {self.name}')
        print(f'The type of cuisine that they offered = {self.cuisine_type}')

    def open(self):
        print(f'{self.name} is opening now')

restaurant = Restoran ('Mang Engking', 'Javanese food')


#Mengeprint untuk describe dan open
restaurant.describe()
restaurant.open()

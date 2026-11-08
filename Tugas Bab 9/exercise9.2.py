class Restoran:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f'Name of the restaurant = {self.name}')
        print(f'The type of cuisine that they offered = {self.cuisine_type}')

    def open(self):
        print(f'{self.name} is opening now')

restaurant1 = Restoran ('Mang Engking', 'Javanese food')
restaurant2 = Restoran ('Kantin Raos Echo', 'Indonesian food')
restaurant3 = Restoran ('Warteg Bahari', 'Javanese food')


#Pakai instance
restaurant1.describe()
restaurant1.open()

print('-'*50)
restaurant2.describe()
restaurant2.open()

print('-'*50)
restaurant3.describe()
restaurant3.open()

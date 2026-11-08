class Restoran:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        print(f'Name of the restaurant = {self.name.title()}')
        print(f'The type of cuisine that they offered = {self.cuisine_type.capitalize()}')

    def open(self):
        print(f'{self.name} is opening now')

class IceCreamStand(Restoran):
    def __init__(self, name, cuisine_type = 'es krim'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def displaying_flavors(self):
        print("\nThis is the flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

eskrim = IceCreamStand('es krim cak mamang')
eskrim.flavors = ['stroberi', 'melon', 'durian']
eskrim.describe()
eskrim.displaying_flavors()

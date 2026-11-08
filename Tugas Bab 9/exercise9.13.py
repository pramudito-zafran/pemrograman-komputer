from random import randint
class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        result = randint (1, self.sides)
        print('result: ', result )
        return result

print("Rolling a 6-sided dice 10 times:")
sisi6 = Dice()  # Menggunakan default sides=6
for hasil in range(10):
    sisi6.roll_dice()
print('-'*35)

# 2. Make a 10-sided die and roll it 10 times
print("Rolling a 10-sided dice 10 times:")
sisi10 = Dice(sides=10)
for hasil in range(10):
    sisi10.roll_dice()
print('-'*35)

# 3. Make a 20-sided die and roll it 10 times
print("Rolling a 20-sided dice 10 times:")
sisi20 = Dice(sides=20)
for hasil in range(10):
    sisi20.roll_dice()
print('-'*35)
    
    

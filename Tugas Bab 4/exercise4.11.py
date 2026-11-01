pizza = ['pepperoni', 'ekstra keju', 'neapolitan']
pizzaTeman = pizza[:]

pizza.append("tuna melt")
pizzaTeman.append('super supreme')

print("Pizza yang saya suka:")
for pizza in pizza:
    print(f"- {pizza}")

print("\nPizza yang teman saya suka :")
for pizza in pizzaTeman:
    print(f"- {pizza}")
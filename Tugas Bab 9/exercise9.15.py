from random import choice

# 1. Membuat possibilities
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# 2. Membuat tiket yang kita punya
my_ticket = [7, 4, 'A', 'C']

# 3. Melakukan pengundian
plays = 0
while True:
    # Mengundi
    tiket_undian = []
    while len(tiket_undian) < 4:
        item = choice(possibilities)
        if item not in tiket_undian:
            tiket_undian.append(item)
    
    plays += 1
    
    # Mengecek apakah tiket kita sama dengan tiket yang diundi
    if sorted(str(isi) for isi in tiket_undian) == sorted(str(isi) for isi in my_ticket):
        break

# 4. Print total pengundian yang dilakukan
print(f"It took {plays} tries to get your winning ticket!")


print("\nVersi 1")
pangkat3 = [nilai**3 for nilai in range(1, 11)]
print(pangkat3)

print("\nVersi 2")
pangkat3 = []
for angka in range(1, 11):
    nilai = angka**3
    pangkat3.append(nilai)
print(pangkat3)
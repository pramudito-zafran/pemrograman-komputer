#Memanipulasi list
tempat = ["dubai", "saudi arabia", "monako"]
print("===Biasa===")
print(tempat)

print("\n===Aturan Alphabet===")
print(sorted(tempat))

print("\n===Biasa===")
print(tempat)

print("\n===Aturan Alphabet-Terbalik===")
print(sorted(tempat, reverse=True))

print("\n===Biasa===")
print(tempat)

print("\n===Terbalik===")
tempat.reverse()
print(tempat)

print("\n===Biasa===")
tempat.reverse()
print(tempat)

print("\n===Aturan Alphabet===")
tempat.sort()
print(tempat)

print("\n===Aturan Alphabet Terbalik===")
tempat.sort(reverse=True)
print(tempat)

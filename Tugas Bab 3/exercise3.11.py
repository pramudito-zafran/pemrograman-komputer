'''barang = ['baju']
print(barang)
print(barang[1])''' 
#Python tidak menemukan apa-apa di index 1 (tidak ada argumen)
#Sehingga muncul "IndexError: list index out of range"

print("===Perbaikan===")
barang = ['baju']
barang.append('bantal')
print(barang[1].title())

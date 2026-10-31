print("====List Makanan====")
makanan = ['martabak', 'ayam goreng', 'takoyaki']
print(makanan)

print("\n====Mencoba Semua Fitur List====")
print("1. " + makanan[0].title())

makanan_1 = f"{makanan[-1].title()}"
print("2. " + makanan_1)

pesan = f'Saya suka makan {makanan[1]}'
print("3. " + pesan)

makanan[1] = 'bakso'
print("4.", makanan)

makanan.append('ayam goreng')
print("5.", makanan)

makanan.insert(2, 'nasi')
print("6.", makanan)

del makanan[2]
print("7.", makanan)

popped_makanan = makanan.pop(1)
print("8.", makanan)
print("  ", popped_makanan.title())

favorit = makanan.pop(0)
print("9. Suka makan", favorit)

makanan.remove('ayam goreng')
print("10.", makanan)

makananJepang = 'takoyaki' 
makanan.remove(makananJepang)
print("11.", makanan)
print(f"    Aku suka {makananJepang}",)

print(f"\n====List Warna====")
warna = ['biru', 'abu-abu', 'kuning']
print(warna)

print(f"\n====Mencoba Semua Fitur List====")
print("1.", sorted(warna))

print("2.", sorted(warna, reverse=True))

warna.reverse()
print("3.", warna)
warna.reverse()

warna.sort()
print("4.", warna)

warna.sort(reverse=True)
print("5.", warna)

len(makanan)
len(warna)

print("5. Jumlah makanan adalah", len(makanan))
print("6. Jumlah warna adalah", len(warna))












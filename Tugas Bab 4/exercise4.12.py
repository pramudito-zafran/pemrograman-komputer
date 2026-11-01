makanan = ['ayam goreng', 'sapi panggang', 'jeroan']
makananTeman = makanan[:]

makanan.append("bakso")
makananTeman.append('sayur labu')

print("Makanan yang saya suka:")
for lauk in makanan:
    print(f"- {lauk}")

print("\nMakanan yang teman saya suka :")
for lauk in makananTeman:
    print(f"- {lauk}")
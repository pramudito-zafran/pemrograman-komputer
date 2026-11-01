menu_makanan = ('sate', 'soto', 'sayur', 'salmon', 'sosis')

print("Silahkan memilih makanan yang ada di menu:")
for makanan in menu_makanan:
    print(f"- {makanan}")

'''menu_makanan.append('bakso')'''
#Tidak bisa diganti karena data berupa tuple, dan tuple tidak mengenal assignment

menu_makanan = ('sate', 'soto', 'sushi', 'sup', 'sarden')#Membuat menu baru
print("\nAda menu baru.")
print("Silahkan memilih makanan yang ada di menu:")
for makanan in menu_makanan:
    print(f"- {makanan}")
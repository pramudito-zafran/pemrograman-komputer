angka_angka = list(range(1, 10))

# Penggunaan == diawali spasi dan diakhiri spasi sehingga mudah dibaca.
for angka in angka_angka:
    if angka == '1': 
        print('1st')
    elif angka == 2:
        print("2nd")
    elif angka == 3:
        print("3rd")
    else:
        print(f"{angka}th")
print('Masukkan dua angka, nantinya dua angka ini akan ditambahkan')
print('Ketik "q" untuk berhenti')

while True:
    angka1 = input('Masukkan angka ke-1: ')
    if angka1 == 'q':
        break

    angka2 = input('Masukkan angka ke-2: ')
    if angka2 == 'q':
        break

    try:
        a1 = int(angka1)
        a2 = int(angka2)
        hasil = a1 + a2
    except ValueError:
        print('Masukkan Angka Yang VALID!')
    else:
        print(hasil)


print('Masukkan dua angka, nantinya dua angka ini akan ditambahkan')

input_pertama = (input('Angka pertama: '))
input_kedua = (input('Angka kedua: '))

try:
    angka1 = int(input_pertama)
    angka2 = int(input_kedua)
    hasil = angka1 + angka2
    print(f'Hasilnya adalah {hasil}')
except ValueError:
    print('Masukkan Angka Yang VALID!')

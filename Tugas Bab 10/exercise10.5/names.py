from pathlib import Path
path = Path('Tugas Bab 10/exercise10.5/guest_book.txt')

print('Masukkan quit untuk memberhentikan program')
isi_file = ''

while True:
    nama = input ('Siapa namamu bang? ').strip().title()

    if nama.lower() == 'quit':
        break
    else:
        isi_file += f'{nama}\n'
 
text = ('===Nama Tamu===\n')
total_isi = text + isi_file

file_guest = path.write_text(total_isi)

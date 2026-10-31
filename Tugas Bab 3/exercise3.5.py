#Masukkan nama" tamu undangan ke variabel tamuUndangan
tamuUndangan = ['joshua', 'zufarul', 'burda']
print(tamuUndangan)

#Menampilkan pesan untuk masing" tamu undangan menggunakan print
print(f"\nYang terhormat Bapak {tamuUndangan[0].title()}, anda kami undang di acara makan malam kami.")
print(f"Halo {tamuUndangan[1].title()}, sudah lama nih kita gak bertatap muka, ayo ikut makan malam bareng kawan-kawan kelas 12.")
print(f"Halo {tamuUndangan[2].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")

#Bapak Joshua tidak bisa datang karena sedang mengajar
print("\nBapak Joshua tidak bisa datang karena sedang mengajar")
del tamuUndangan[0]
print(tamuUndangan)

#Memasukkan orang lain
print("\nMengundang Fadil untuk datang ke acara makan malam")
tamuUndangan.insert(0, 'Fadil')
print(tamuUndangan)

#Menampilkan pesan untuk masing" tamu undangan menggunakan print
print(f"\nYang terhormat Bapak {tamuUndangan[0].title()}, anda kami undang di acara makan malam kami.")
print(f"Halo {tamuUndangan[1].title()}, sudah lama nih kita gak bertatap muka, ayo ikut makan malam bareng kawan-kawan kelas 12.")
print(f"Halo {tamuUndangan[2].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")

tamuUndangan = ['joshua', 'zufarul', 'burda']
print(tamuUndangan)

#Menampilkan pesan untuk masing" tamu undangan menggunakan print
print(f"\nYang terhormat Bapak {tamuUndangan[0].title()}, anda kami undang di acara makan malam kami.")
print(f"Halo {tamuUndangan[1].title()}, sudah lama nih kita gak bertatap muka, ayo ikut makan malam bareng kawan-kawan kelas 12.")
print(f"Halo {tamuUndangan[2].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")


#Bapak Joshua tidak bisa datang karena sedang mengajar
print('\n"Bapak Joshua tidak bisa datang karena sedang mengajar"')
del tamuUndangan[0]
print(tamuUndangan)

#Memasukkan orang lain
print('\n"Mengundang orang lain untuk menggantikan Bapak Joshua"')
tamuUndangan.insert(0, 'fadil')
print(tamuUndangan)

#Menampilkan pesan untuk masing" tamu undangan menggunakan print
print(f"\nYang terhormat Bapak {tamuUndangan[0].title()}, anda kami undang di acara makan malam kami.")
print(f"Halo {tamuUndangan[1].title()}, sudah lama nih kita gak bertatap muka, ayo ikut makan malam bareng kawan-kawan kelas 12.")
print(f"Halo {tamuUndangan[2].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")

#Menambah orang-orang baru karena meja makannya besar dan masih ada tempat untuk orang lain
print('\n"Ternyata ada meja besar yang akan datang. Ada tempat untuk 3 orang lagi"')
tamuUndangan.insert(0, "leon")
tamuUndangan.insert(2, "kennedy")
tamuUndangan.append("jill")


print(tamuUndangan)

print(f"\nYang terhormat Bapak {tamuUndangan[0].title()}, anda kami undang di acara makan malam kami.")
print(f"Halo {tamuUndangan[1].title()}, sudah lama nih kita gak bertatap muka, ayo ikut makan malam bareng kawan-kawan kelas 12.")
print(f"Halo {tamuUndangan[2].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")
print(f"Halo {tamuUndangan[3].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")
print(f"Halo {tamuUndangan[4].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")
print(f"Halo {tamuUndangan[5].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")

#Meja besarnya belum datang jadi hanya bisa invite 2 orang saja
print('\n"Maaf untuk para tamu undangan, saya hanya bisa mengajak 2 orang saja karena meja besarnya belum datang"')
tamu_undangan6 = tamuUndangan.pop()
tamu_undangan5 = tamuUndangan.pop()
tamu_undangan4 = tamuUndangan.pop()
tamu_undangan3 = tamuUndangan.pop()

print(f"\nMaaf {tamu_undangan6.title()}, aku tidak bisa mengundang kamu karena tempatnya sudah penuh")
print(f"Maaf {tamu_undangan5.title()}, aku tidak bisa mengundang kamu karena tempatnya sudah penuh")
print(f"Maaf {tamu_undangan4.title()}, aku tidak bisa mengundang kamu karena tempatnya sudah penuh")
print(f"Maaf {tamu_undangan3.title()}, aku tidak bisa mengundang kamu karena tempatnya sudah penuh")

print('\n"Yang tersisa hanya Leon dan Fadil"')
print(tamuUndangan)

print(f"\nHalo {tamuUndangan[0].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")
print(f"Halo {tamuUndangan[1].title()}, ayo main ke rumahku, di tempatku ada sarasehan nanti malam.")
del tamuUndangan[0]
del tamuUndangan[0]

print('\n"Tamu undangan tersisa 0"')
print(tamuUndangan)
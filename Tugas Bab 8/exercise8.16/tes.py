#Versi 1
import salam
salam.tampilkan_pesan()

#Versi 2
from salam import tampilkan_pesan
tampilkan_pesan()

#Versi 3
from salam import tampilkan_pesan as tp
tp()

#Versi 4
import salam as s
s.tampilkan_pesan()

#Versi 5
from salam import *
tampilkan_pesan()

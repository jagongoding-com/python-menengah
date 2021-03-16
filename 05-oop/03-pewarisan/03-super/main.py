from Orang import Orang
from Pekerja import Pekerja
from Pelajar import Pelajar

andi = Orang('Andi', 'Surabaya')
andi.perkenalan()

deni = Pelajar('Deni', 'Makassar', 'SMA Negeri 1 Makassar')
deni.perkenalan()
print(f'Saya sekolah di {deni.sekolah}')

budi = Pekerja('Budi', 'Pontianak', 'Google')
budi.perkenalan()
print(f'Saya bekerja di {budi.tempat_kerja}')

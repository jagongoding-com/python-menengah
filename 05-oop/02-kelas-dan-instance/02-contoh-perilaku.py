# buat kelasnya terlebih dahulu
class Mahasiswa:
  nama = None
  asal = None

  def perkenalan (self):
    print(f'Perkenalkan saya {self.nama} dari {self.asal}')

deni = Mahasiswa()
deni.nama = "Deni"
deni.asal = "Jawa Timur"

lendis = Mahasiswa()
lendis.nama = "Lendis Fabri"
lendis.asal = "Jawa Timur"

deni.perkenalan()
lendis.perkenalan()

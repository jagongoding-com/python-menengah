class Mahasiswa:
  def __init__(self, nama, asal):
    self.nama = nama
    self.asal = asal

  def perkenalan (self):
    print(f'Perkenalkan saya {self.nama} dari {self.asal}')

deni = Mahasiswa('Deni', 'Sulawesi')
lendis = Mahasiswa(asal = 'Sumatera', nama = 'Lendis Fabri')

deni.perkenalan()
lendis.perkenalan()
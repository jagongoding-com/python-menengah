class Orang:

  def __init__ (self, nama, asal):
    self.nama = nama
    self.asal = asal
    print('fungsi Orang.__init__() dieksekusi')

  def perkenalan (self):
    print(f'Perkenalkan nama saya {self.nama} dari {self.asal}')


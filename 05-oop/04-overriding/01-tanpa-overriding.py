class Kendaraan:
  def berjalan(self):
    print('berjalan..')

class Mobil(Kendaraan):
  def berjalan(self):
    print('Berjalan dengan cepat..')

sepeda = Kendaraan()
sedan = Mobil()

sepeda.berjalan()
sedan.berjalan()

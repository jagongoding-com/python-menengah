class Kendaraan:
  def berjalan(self):
    print('berjalan..')

class Mobil(Kendaraan):
  def berjalan(self, kecepatan, satuan = 'km/j'):
    print(f'Berjalan dengan kecepatan {kecepatan} {satuan}')

sepeda = Kendaraan()
sedan = Mobil()

sepeda.berjalan()
sedan.berjalan(150)

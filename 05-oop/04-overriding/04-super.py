class Kendaraan:
  def berjalan(self):
    print('berjalan..')

class Mobil(Kendaraan):
  def berjalan(self, kecepatan, satuan = 'km/j'):
    super().berjalan()
    print(f'  -> dengan kecepatan {kecepatan} {satuan}')

sepeda = Kendaraan()
sedan = Mobil()

sepeda.berjalan()
sedan.berjalan(150)

class Kucing:
  def __init__(self, warna, usia):
    self.warna = warna
    self.usia = usia

class Mahasiswa:
  def __init__(self, nama, asal, kucing):
    self.nama = nama
    self.asal = asal
    self.kucing = kucing

  def perkenalan(self):
    print(f'Perkenalkan saya {self.nama} dari {self.asal}')
    print(f'Saya memiliki kucing berwarna {self.kucing.warna} usia {self.kucing.usia}')

deni = Mahasiswa(
    nama='Deni',
    asal='Sidoarjo',
    kucing=Kucing(
        warna='Merah',
        usia='3 bulan'
    )
)

deni.perkenalan()

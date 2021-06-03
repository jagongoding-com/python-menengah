class Mahasiswa:
  def __init__(self, nama):
    self.nama = nama
    print(f'mahasiswa {self.nama} dibuat')

  def __del__(self):
    print(f'mahasiswa {self.nama} dihapus')

budi = Mahasiswa('budi')
andi = Mahasiswa('andi')

del andi
del budi
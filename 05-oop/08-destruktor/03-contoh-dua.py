class Mahasiswa:
  def __init__(self, nama):
    self.nama = nama
    print(f'mahasiswa {self.nama} dibuat')

  def __del__(self):
    print(f'mahasiswa {self.nama} dihapus')

print('Halo dunia')
budi = Mahasiswa('budi')
print('Halo semuanya')
andi = Mahasiswa('andi')
print('1 + 1 = 2')
print('3 + 3 = 6')
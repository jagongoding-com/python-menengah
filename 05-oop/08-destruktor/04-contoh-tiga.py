class Mahasiswa:
  def __init__(self, nama):
    self.nama = nama
    print(f'mahasiswa {self.nama} dibuat')

  def __del__(self):
    print(f'mahasiswa {self.nama} dihapus')

mahasiswaX = Mahasiswa('Budi')
mahasiswaX = 10 # Budi kehilangan referensi

print(f'mahasiswaX = {mahasiswaX}')
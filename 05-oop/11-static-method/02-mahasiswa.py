class Mahasiswa:
  def __init__(self, nama):
    self.__nama = nama

  def getNama(self):
    return self.__nama

  @staticmethod
  def hurufBesar(nama):
    return nama.upper()

budi = Mahasiswa('Budi')
print(budi.getNama())
print(Mahasiswa.hurufBesar(budi.getNama()))
# parameter bisa dari luar kelas
print(Mahasiswa.hurufBesar("andi hartanto"))
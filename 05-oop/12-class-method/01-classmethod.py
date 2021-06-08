class Manusia:
  jumlah_tangan = 2 # class variable

  def __init__(self, nama):
    self.nama = nama # instance variable

  @classmethod
  def pengertian(cls):
    print(f'Manusia memilki {cls.jumlah_tangan} tangan')

# panggil secara langsung
Manusia.pengertian()
# panggil via objek
seseorang = Manusia('Tanpa Nama')
seseorang.pengertian()
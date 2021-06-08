from datetime import date

class Mahasiswa:
  def __init__(self, nama, usia):
    self.nama = nama
    self.usia = usia

  @classmethod
  def berdasarkanTahunLahir(cls, nama, tahunLahir):
    tahunSekarang = date.today().year
    usia = tahunSekarang - tahunLahir

    # buat instan dengan konstruktor asli
    return cls(nama, usia)

  @staticmethod
  def apakahSudahTua(usia):
    return usia > 35

  def __str__(self):
    return f'{self.nama} usia {self.usia} tahun'

# cara 1:
wahid = Mahasiswa("Wahid Abdullah", 25)
print(wahid)
# cara 2:
lendis = Mahasiswa.berdasarkanTahunLahir("Lendis Fabri", 1995)
print(lendis)

print("apakah usia 40 sudah tua?", Mahasiswa.apakahSudahTua(40))
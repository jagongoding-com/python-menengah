class Konversi:

  @staticmethod
  def satuan_ke_lusin(n):
    return n / 12

  @staticmethod
  def satuan_ke_klodi(n):
    return n / 20

  @staticmethod
  def satuan_ke_gross(n):
    return n / 144

n = 54
print(Konversi.satuan_ke_lusin(n))
print(Konversi.satuan_ke_klodi(n))
print(Konversi.satuan_ke_gross(n))
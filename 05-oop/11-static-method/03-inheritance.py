class Manusia:
  def __init__(self, nama):
    self.__nama = nama

  def getNama(self):
    return self.__nama

  @staticmethod
  def namaBesar(nama):
    return nama.upper()

class LakiLaki(Manusia): # mewarisi Manusia
  def __init__(self, nama):
    super().__init__(nama)

  def getNama(self):
    return Manusia.namaBesar(super().getNama())

suwarno = Manusia('suwarno')
print(suwarno.getNama())
sutejo = LakiLaki('Sutejo')
print(sutejo.getNama())
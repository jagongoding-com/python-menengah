from Orang import Orang

class Pekerja (Orang):
  def __init__ (self, nama, asal, tempat_kerja):
    Orang.__init__(self, nama, asal)
    self.tempat_kerja = tempat_kerja

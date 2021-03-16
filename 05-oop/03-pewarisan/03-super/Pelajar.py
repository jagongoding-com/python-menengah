from Orang import Orang

class Pelajar (Orang):
  def __init__ (self, nama, asal, sekolah):
    super().__init__(nama, asal)
    self.sekolah = sekolah

class Siswa:
  def __init__(self):
    self.__list_siswa = []

  def tambah_siswa(self, siswa):
    self.__list_siswa.append(siswa)

  def __len__(self):
    return len(self.__list_siswa)

  def __getitem__(self, position):
    return self.__list_siswa[position]

grup1 = Siswa()
grup1.tambah_siswa('Huda')
grup1.tambah_siswa('Wahid')

print(grup1[0])

# bisa juga pakai for
for siswa in grup1:
  print(siswa)
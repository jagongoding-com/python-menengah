class Mahasiswa:
  # static atau class variable
  jenjang = 'S1'

  def __init__(self, nama):
    # instance variable
    self.nama = nama

budi = Mahasiswa('Budi')
print(budi.jenjang)

andi = Mahasiswa('Andi')
print(andi.jenjang)

Mahasiswa.jenjang = 'S3'

print(andi.jenjang)
print(budi.jenjang)
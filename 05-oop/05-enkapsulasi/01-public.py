class Segitiga:

  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi
    self.luas = 0.5 * alas * tinggi 


segitiga_besar = Segitiga(100, 80)

# akses variabel alas, tinggi, dan luas dari luar kelas
print(f'alas: {segitiga_besar.alas}')
print(f'tinggi: {segitiga_besar.tinggi}')
print(f'luas: {segitiga_besar.luas}')
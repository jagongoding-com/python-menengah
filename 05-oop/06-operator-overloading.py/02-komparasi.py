class Angka:
  def __init__(self, angka):
    self.angka = angka

  def __gt__(self, objek):
    return self.angka > objek.angka

  def __lt__(self, objek):
    return self.angka < objek.angka

  def __eq__(self, objek):
    return self.angka == objek.angka

x1 = Angka(20)
x2 = Angka(10)

print(x1 > x2)
print(x1 < x2)
print(x1 == x2)
class Induk1:
  pass

class Induk2:
  pass

class Turunan(Induk1, Induk2):
  pass

print(Turunan.__mro__)
print(Turunan.mro())
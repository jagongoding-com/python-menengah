class Contoh:

  def __str__(self):
    return 'bentuk informal'

  def __repr__(self):
    return 'bentuk formal'

x = Contoh()
print(x)
print(str(x))
print(repr(x))
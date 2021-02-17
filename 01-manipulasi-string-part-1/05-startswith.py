nomor_telepon_1 = '0871122334455'
nomor_telepon_2 = '6288776655300'
nomor_telepon_3 = '+6233003300330'

kode_negara = '+62'
print(nomor_telepon_1.startswith(kode_negara)) # False
print(nomor_telepon_2.startswith(kode_negara)) # False
print(nomor_telepon_3.startswith(kode_negara)) # True
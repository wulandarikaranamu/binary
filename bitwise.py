#operator bitwise(biner/binary)

#bitwise or (|)
data = 8
angka = 4
hasil = data | angka
print("==========or==========")
print("nilai :",data,"binary :",format(data,'08b'))
print("nilai :",angka,"binary :",format(angka,'08b'))
print("----------(|)---------")
print("nilai :",hasil,"binary :",format(hasil,'08b'))

#bitwise and (&)
hasil = data & angka
print("==========and==========")
print("nilai :",data,"binary :",format(data,'08b'))
print("nilai :",angka,"binary :",format(angka,'08b'))
print("----------(&)---------")
print("nilai :",hasil,"binary :",format(hasil,'08b'))

#bitwise XOR (^)
hasil = data ^ angka
print("==========XOR==========")
print("nilai :",data,"binary :",format(data,'08b'))
print("nilai :",angka,"binary :",format(angka,'08b'))
print("----------(^)---------")
print("nilai :",hasil,"binary :",format(hasil,'08b'))

#bitwise NOT (~)
hasil = ~data
print("==========NOT==========")
print("nilai :",data,"binary :",format(data,'08b'))
print("----------(~)---------")
print("nilai :",hasil,"binary :",format(hasil,'08b'))

print("-----------untuk membuat not(^)-----------")

pembilang =0b001110
penyebut =0b100110
print("nilai :",pembilang^penyebut,"binary :",format(pembilang^penyebut,'08b'))

#shifting
#shift right(>>)
hasil = data >> 1
print("==========shift right==========")
print("nilai :",data,"binary :",format(data,'08b'))
print("----------(>>)---------")
print("nilai :",hasil,"binary :",format(hasil,'08b'))

#shift left(>>)
hasil = data >> 1
print("==========shift left==========")
print("nilai :",data,"binary :",format(data,'08b'))
print("------------(<<)-----------")
print("nilai :",hasil,"binary :",format(hasil,'08b'))
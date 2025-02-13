import math

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

keliling = 2 * math.pi * jari_jari
luas = math.pi * (jari_jari ** 2)

print("Keliling lingkaran:", int(keliling))
print("Luas lingkaran:", int(luas))

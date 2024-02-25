print("Aplikasi menghitung luas dan volume Limas Segiempat")

# Atur nilai variabel
sisi = 6
alas = 8
tinggi = 10

# Rumus
luas_sisi = 4*alas*tinggi
luas_alas = sisi*sisi
luas = luas_sisi+luas_sisi+luas_sisi+luas_sisi+luas_sisi
volume = luas_alas * tinggi / 3

#output
print("Sisi = ",sisi)
print("Alas = ",alas)
print("Luas Sisi = ",luas_sisi)
print("Luas Alas = ",luas_alas)
print("Tinggi = ",tinggi)
print("Luas = ",luas)
print("Volume = ",volume)
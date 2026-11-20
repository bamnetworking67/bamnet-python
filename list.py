# list kosong
daftar_kosong = []

# list dengan angka
angka = [1, 2, 3, 4, 5]
angka.append(6)
angka.append(7)
angka.append(8)
angka.append(9)
angka.remove(2)
angka.pop()
del angka[5]
print(len(angka))
print(angka)

# list dengan string
nama = ["iqbal", "titis", "galih", "kasya", "dinda", "anisa", "maul"]
nama.append("vito")   # Menambahkan list
nama.remove("vito")   # Menghapus list
del nama[3]
print(len(nama))


# list campuran
anggota_bamnet = [12, "jibran", 11, "zefran", 10, "maul"]
print(nama)
print(anggota_bamnet)

buah1 = ["durian", "apel", "mangga"]
buah2 = ["kelengkeng", "pir", "pepaya"]
buah_doang = buah1 + buah2
print(buah_doang)

# menggunakan for loop
print("Daftar buah:")
for item in buah_doang:
    print("-", item)

print(buah1[2])
print(angka[4])
buah_doang[3]= "pisang"
print(buah_doang)
buah_doang[5] = "nanas"
print(buah_doang)
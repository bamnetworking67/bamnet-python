# Mencetak angka 1 sampai 5
angka = 1
while angka <= 5:
    print(angka)
    angka += 1

password = ""
while password != "123456":
    password = input("Masukkan password: ")
    if password != "123456":
        print("Password salah, coba lagi!")

print("Password benar")
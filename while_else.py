# Mencari pw yg benar dgn batas percobaan
pw_benar = "123456"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    pw = input("Masukkan pw: ")
    percobaan += 1

    if pw == pw_benar:
        print("Login berhasil")
        break
    else:
        print("Pw salah. Sisa percobaan:", max_percobaan - percobaan)
else:
    print("Wah hacker yaa lu")
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "123456":
        print("Yeayyyy, login berhasil")
        print("Selamat datang admin")
    else:
        print("Password salah")
else:
    print("Salah semuanya")
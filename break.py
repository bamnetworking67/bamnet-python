angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka(1-10): "))

    if tebakan == angka_rahasia:
        print("Selamat brok")
        break
    else:
        print("Salah, pasti ijazahnya palsu")
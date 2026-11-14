harga_kopi = 15000
saldo_vito = int(input("Saldo: "))
mesin_rusak = False

# Logika
if saldo_vito >= harga_kopi and (not mesin_rusak):
    print('Kopi Keluar!')
    saldo_vito = saldo_vito - harga_kopi
elif saldo_vito >= harga_kopi or mesin_rusak:
    print("Maaf, mesin rusak, saldo tidak dipotong")
elif saldo_vito >= 0 and saldo_vito < harga_kopi:
    kurang = harga_kopi - saldo_vito
    print("Saldo kurang Rp", kurang)
else:
    print("Error Sistem")
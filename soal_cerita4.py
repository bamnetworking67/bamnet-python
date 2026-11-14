ban_berjalan = ["Kertas", "Batu", "Plastik", "Bom", "Plastik", "Kertas"]
sampah_terproses = 0

for barang in ban_berjalan:
    if barang == "Batu":
        print("Mendeteksi batu, lewati.....")
        continue  # Lewati dan masuk ke program selanjutnya
    elif barang == "Bom":
        print("WOY LARI WOYYY")
        break # Berhenti darurat

    print("Memproses", barang)
    sampah_terproses += 1

print("Total sampah diproses: ", sampah_terproses) # isi total sampah yang di proses oleh robot


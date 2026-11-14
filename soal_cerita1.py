bebek_jantan = 63
bebek_betina = 192

# setelah bulan pertama
bebek_betina = bebek_betina + bebek_jantan
bebek_jantan = bebek_jantan - (bebek_jantan // 3)

# setelah bulan kedua
bebek_jantan = bebek_jantan + bebek_betina
bebek_betina = bebek_betina - 10

#total banyaknya bebek pak Dengklek after bulan ke dua
total = bebek_betina + bebek_jantan
print(total)
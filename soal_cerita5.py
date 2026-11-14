ukuran = 5

for i in range(ukuran):
    for j in range(ukuran):
        if i == j:
            print("X", end="")
        else:
            print("-", end="")
    print(ukuran)
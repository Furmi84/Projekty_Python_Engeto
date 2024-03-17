while (hodnota:= input("Zadej cislo:")):
    print(f"{hodnota}")
    if hodnota.isdigit():
        print("je to čislo")
        break
    else:
        print("Neni to čislo")
        continue
print(f"{hodnota=}")
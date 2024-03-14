slova = set()
while len(slova) < 3:
    slovo = input("Zadej slovo: ")
    if slovo in slova:
        print(f"Slovo {slovo} už je uložené")
    else:
        if len(slovo) != 4:
            print("Slovo není dlouhé čtyři znaky")
        else:
            slova.add(slovo)
    print(len(slova))

else:
    print("Už mám uložené tří slova")
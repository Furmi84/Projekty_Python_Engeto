"""projekt_c2.py: druhy projekt do Engeto Online Python Akademie.

author: Martin Furmanek
email: martin.furmanek@gmail.com
discord: Furmi84

"""

import os
import random

#os.system("cls")

def generovat_cislo():
    # První číslo z rozsahu 1-9
    prvni = random.choice(range(1, 10))

    # Zbývající čísla z rozsahu 0-9, vyjma prvního čísla
    mozna_cisla = list(range(0, 10))
    mozna_cisla.remove(prvni)
    zbyvajici = random.sample(mozna_cisla, 3)

    # Kombinace prvního čísla se zbyvajícími
    cislo = str(prvni) + ''.join(map(str, zbyvajici))

    return cislo
def zadavani_cisla():
    dotazovani = True

    while dotazovani:
        odpoved = input("Zadej celé číslo od 1 do 5")

        if odpoved.isnumeric() and int(odpoved) in range(1, 6):
            print("Výborně")
            dotazovani = False
        else:
            print("Špatná hodnota, zkus to znovu")

            # Kontrola, jestli zadaný údaj je číslo
            if not zadane_cislo_hracem.isdigit():
                print("zadaný údaj není číslo")
            # Kontrola, jestli zadané číslo začíná nulou
            elif zadane_cislo_hracem[0] == "0":
                print("zadané číslo začíná nulou")
            # Kontrola délky zadaného čísla
            elif len(zadane_cislo_hracem) != 4:
                print("zadané číslo nemá přesně 4 znaky")

            duplicita_znaku = 0

            for znak in zadane_cislo_hracem:
                #       print("Znak",znak)
                if zadane_cislo_hracem.count(znak) > 1:
                    duplicita_znaku += 1
                if duplicita_znaku >= 2:
                    print("Zadané číslo obsahuje duplicitu čisel")
        return odpoved
def hraj(cislo_od_hrace,cislo_od_pc):
    bulls = 0
    cows = 0
    pocet_opakovani = 0
    for a in cislo_od_hrace:
        for b in cislo_od_pc:
            if a == b:
                if cislo_od_pc.index(b) == cislo_od_hrace.index(a):
                    bulls += 1
                else:
                    cows += 1

    text_bulls = "bulls " if bulls >= 2 else "bull "
    text_cows = "cows " if cows >= 2 else "cows "

    print(f"{text_bulls}{bulls}, {text_cows}{cows}")
    return bulls,cows


print("Ahoj.")
print("-"*50)
print("Vygeneroval jsem pro tebe nahodno číslo.")
print("Pojdmě si zahrát hru na býky a krávy.")
print("-"*50)

os.system("cls")

# inicializace proměnych
pocet_opakovani = 0
zadane_cislo_pocitacem = generovat_cislo()
byci = 0
kravy = 0

while True:
    zadane_cislo_hracem = zadavani_cisla()
    delka_zadaneho_cisla = len(zadane_cislo_hracem)
    #print("delka zadaneho cisla",delka_zadaneho_cisla)
    print("-"*50)
    print("Zadane cislo hracem",zadane_cislo_hracem)
    print("Zadane cislo pocitacem",zadane_cislo_pocitacem)
    #print(zadane_cislo_hracem[0])



    byci,kravy = hraj(zadavani_cisla(), zadane_cislo_pocitacem)
    #print(f"{pocet_opakovani=}")
    if byci == 4:
        pocet_opakovani += 1
        print(f"Skvěle vyhral jsi. Počet opakovani je {pocet_opakovani}")
        exit()
    else:
        pocet_opakovani += 1

   


     
    

    

        



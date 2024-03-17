"""projekt_c2.py: druhy projekt do Engeto Online Python Akademie.

author: Martin Furmanek
email: martin.furmanek@gmail.com
discord: Furmi84

"""

import os
import random
import time

os.system("cls")


def generovat_cislo():
    """Return the latitude and longitude values of the waypoint."""
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
    """Return the latitude and longitude values of the waypoint."""
    while hodnota := input("Zadej cislo:"):

        # Set pro sledování již viděných znaků
        videne_znaky = set()

        # Proměnná pro detekci duplicity
        duplicita_nalezena = False

        for znak in hodnota:
            # Pokud jsme již znak viděli, nastavíme duplicita_nalezena na True a vypíšeme zprávu
            if znak in videne_znaky:
                duplicita_nalezena = True
                break  # Přerušení cyklu po nalezení první duplicity
            else:
                videne_znaky.add(znak)  # Přidání znaku do sledovaných, pokud jsme ho ještě neviděli

        # Pokud nebyla nalezena žádná duplicita
        if duplicita_nalezena:
            print("Zadané číslo obsahuje duplicitu čísel.")
            continue
        # Kontrola, jestli zadaný údaj je číslo
        elif not hodnota.isdigit():
            print("Zadana hodnota není čislo")
            continue
        # Kontrola, jestli zadané číslo začíná nulou
        elif hodnota[0] == "0":
            print("Zadané číslo začíná nulou")
            continue
        # Kontrola délky zadaného čísla
        elif len(hodnota) != 4:
            print("zadané číslo nemá přesně 4 znaky")
            continue
        else:
            return hodnota


def vypocet_bulls_and_cows(hrac, pocitac):
    """vypocet hry bulls and cows, vstupy jsou hodnoty od hrace a od pocitace."""
    byci = 0
    kravy = 0

    for x in range(len(hrac)):
        # pokud je cislice od hrace na pozici rovno cislici pocitace na pozici
        if hrac[x] == pocitac[x]:
            byci += 1
        # pokud je cislice na pozici obsazena v promene pocitac
        elif hrac[x] in pocitac:
            kravy += 1

    return byci, kravy


print("Ahoj.")
print("-"*50)
print("Vygeneroval jsem pro tebe nahodno číslo.")
print("Pojdmě si zahrát hru na býky a krávy.")
print("-"*50)
print("""Bulls and Cows: Uhádni 4-místné číslo (bez duplicit). 
Dostaneš nápovědu:
Byci (správné číslice na správných pozicích) 
Krávy (správné číslice na špatných pozicích). 
Hádej dál, dokud neuhodneš!""")
print("-"*50)
# inicializace proměnych
pocet_opakovani = 0
zadane_cislo_pocitacem = generovat_cislo()
zacatek = time.time()

while True:

    zadane_cislo_hracem = zadavani_cisla()
    print("-"*50)
    print("Zadane cislo hracem: ", zadane_cislo_hracem)

    bulls, cows = vypocet_bulls_and_cows(zadane_cislo_hracem, zadane_cislo_pocitacem)

    text_bulls = "Byci " if bulls >= 2 else "Býk"
    text_cows = "Krávy " if cows >= 2 else "Kráva"

    print(f"{bulls} {text_bulls}, {cows} {text_cows}")

    if bulls == 4:
        pocet_opakovani += 1
        konec = time.time()
        print(f"Skvěle vyhral jsi. Počet opakovani je {pocet_opakovani}.")
        print(f"Trvalo ti to přesně {int(konec - zacatek)} sekund")
        break
    else:
        pocet_opakovani += 1

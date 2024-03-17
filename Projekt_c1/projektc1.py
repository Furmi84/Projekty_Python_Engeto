"""projekt_1.py: první projekt do Engeto Online Python Akademie.

author: Martin Furmanek
email: martin.furmanek@gmail.com
discord: Furmi84

"""
import re
import os

os.system("cls")

TEXTS = ['''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''']


def vykresleni_dekorace():
    """Funkce slouzi pro dekoraci."""
    znak = "-"
    pocet = 50
    print(znak * pocet)


def prihlaseni_do_systemu():
    """Funkce slouzi pro prihlaseni do systemu."""
    uzivatele = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"
    }

    vykresleni_dekorace()
    zadane_jmeno = input("Zadej prosim te sve uzivatelske jmeno? ")
    vykresleni_dekorace()
    zadane_heslo = input("Zadej prosim te heslo? ")
    vykresleni_dekorace()

    if zadane_heslo == uzivatele.get(zadane_jmeno):
        print(f"Prihlaseni probehlo uspesne. Vitej {zadane_jmeno}")
        vykresleni_dekorace()
        return True
    else:
        print("Prihlaseni je neuspesne, ukončuji program.\n")
        exit()


if prihlaseni_do_systemu():

    volba_textu = input(f"Zvol si text, 1 až {len(TEXTS)}? ")

    if volba_textu.isdigit():
        volba_textu_cislo = int(volba_textu)
        if 1 <= volba_textu_cislo <= len(TEXTS):
            zadany_text = TEXTS[volba_textu_cislo - 1]
        else:
            print(f"Tvá volba zvoleného textu je mimo rozsah. Ukončuji program.")
            exit()
    else:
        print("Zadaná volba není číslo. Ukončuji program.")
        exit()

    vykresleni_dekorace()
    print(f"Zadany text \n {zadany_text} \n")
    vykresleni_dekorace()

    # uprava textu
    """ jen_slova = re.findall(r'\b[a-zA-Z0-9]+\b', zadany_text) -
         tento regularni vyraz filtruje pouze slova ... viz 'the', 'valley'"""
    jen_slova = zadany_text.split()
    # rozdeli slova pouze podle mezer, nechava tecky u slov ... viz  'the', 'valley.'
    # print(jen_slova)
    velikost_jen_slova = len(jen_slova)
    cislice_v_textu = re.findall(r'\d+', zadany_text)
    vykresleni_dekorace()

    # vypsani vysledku
    pocet_velkych = 0
    pocet_s_velkym_zacatkem = 0
    pocet_malych = 0

    for slovo in jen_slova:
        if slovo.isupper():
            pocet_velkych += 1
        elif slovo.istitle():
            pocet_s_velkym_zacatkem += 1
        elif slovo.islower():
            pocet_malych += 1

    # Pro cislice_v_textu předpokládám, že je seznam číselných řetězců.
    pocet_cisel = sum(1 for cislo in cislice_v_textu if cislo.isdigit())
    suma_cisel = sum(int(cislo) for cislo in cislice_v_textu)

    print(f"Pocet slov: {len(jen_slova)}")
    print(f"Pocet slov s velkymi pismeny: {pocet_velkych}")
    print(f"Pocet slov s velkymi pismeny na zacatku: {pocet_s_velkym_zacatkem}")
    print(f"Pocet slov s malymi pismeny: {pocet_malych}")
    print(f"Pocet cisel v textu: {pocet_cisel}")
    print(f"Suma cisel v textu: {suma_cisel}")

    # vypocet dat do tabulky / vykresleni tabulky
    vykresleni_dekorace()

    # Použití slovníku pro sledování počtu slov podle jejich délky
    delka_slov = {}

    # Naplnění slovníku, kde klíč je délka slova a hodnota je počet slov této délky
    for slovo in jen_slova:
        delka_slov[len(slovo)] = delka_slov.get(len(slovo), 0) + 1

    # Iterace přes slovník a výpis statistik
    for delka, pocet in sorted(delka_slov.items()):
        print("{:^5}|{:<20}|{:^10}|".format(delka, "*" * pocet, pocet))

    vykresleni_dekorace()

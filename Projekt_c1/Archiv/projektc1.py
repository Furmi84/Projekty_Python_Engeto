"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Martin Furmanek
email: martin.furmanek@gmail.com
discord: Furmi84
"""
import re

def vykresleni_dekorace():
  znak = "-"
  pocet = 50
  print (znak * pocet)

def prihlaseni_do_systemu():

  uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
  }

  try:
    vykresleni_dekorace()
    zadane_jmeno = input("Zadej prosim te sve uzivatelske jmeno? ")
    vykresleni_dekorace()
    zadane_heslo = input("Zadej prosim te heslo? ")
    vykresleni_dekorace()
    if zadane_heslo == uzivatele[zadane_jmeno]:
      print (f"Prihlaseni probehlo uspesne. Vitej {zadane_jmeno}")
      vykresleni_dekorace()
      return True
    else:
      print ("Prihlaseni je neuspesne")
      return False
  except KeyError:
    print ("Zadane uzivatelske jmeno je neplatne")
    return False

def prace_s_textem():
  TEXTS = [''' ''','''
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
    garpike and stingray are also present.'''  ]

  try:
    return TEXTS[int(input("Zvol si text, 1,2 a nebo 3? " ))]
  except IndexError:
    print ("Zadana hodnota je neplatna")

if prihlaseni_do_systemu():

  zadany_text = prace_s_textem()
  vykresleni_dekorace()
  print (f"Zadany text \n {zadany_text} \n")
  vykresleni_dekorace()

  # uprava textu
  jen_slova = re.findall(r'\b[a-zA-Z0-9]+\b', zadany_text)
  cislice_v_textu = re.findall(r'\d+', zadany_text)

  vykresleni_dekorace()
  
  # vypsani vysledku
  print (f"Pocet slov {len(jen_slova)}")
  print (f"Pocet slov s velkymi pismeny {sum(1 for znak in jen_slova if znak.isupper())}")
  print (f"Pocet slov s velkymi pismeny na zacatku {sum(1 for znak in jen_slova if znak.istitle())}")
  print (f"Pocet slov s malymi pismeny {sum(1 for znak in jen_slova if znak.islower())}")
  print (f"Pocet cisel v textu {sum(1 for cisla in cislice_v_textu if cisla.isdigit())}")
  print (f"Suma cisel v textu {sum(int(cisla) for cisla in cislice_v_textu)}")

  # vypocet dat do tabulky / vykresleni tabulky
  vysledek = [0]
  vykresleni_dekorace()
  print("{:^5}|{:^20}|{:^10}|".format("Delka","Pocet vyskytu","Pocet"))
  vykresleni_dekorace()
  for index in range (1,12):
    vysledek.insert(index,sum(1 for znak in jen_slova if len(znak)==index))
    print("{:^5}|{:<20}|{:^10}|".format(index,"*"*vysledek[index],vysledek[index]))

vykresleni_dekorace()








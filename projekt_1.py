def prihlaseni_do_systemu ():

  thisdict = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
  }

  try:
    zadane_jmeno = input("Zadej prosim te sve uzivatelske jmeno? ")
    zadane_heslo = input("Zadej prosim te heslo? ")
    if zadane_heslo == thisdict[zadane_jmeno]:
      print ("Prihlaseni probehlo uspesne")
      return True
    else:
      print ("Heslo je zadane nespravne")
      return False
  except KeyError:
    print ("Zadane uzivatelske jmeno je neplatne")
    return False

def prace_s_textem():
  TEXTS = ['''pokusny text 10 20 30 Ahoj Blbe ''','''
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
    return TEXTS[int(input("Zvol si text, 1,2 a nebo 3 ? "))]
  except IndexError:
    print ("Zadana hodnota je neplatna")

#vysledek = prihlaseni_do_systemu()
def analyza_textu(text):
  slova = text.split()
  print (f"Zvoleny text {slova}")
  slova_male_pismena = 0
  cislice = 0
  slova_zacatek_velky = 0
  soucet_cislic = 0

  for jednotliva_slova in slova:
    if jednotliva_slova.islower():
      slova_male_pismena += 1
      #print (f"Zvoleny text {slova_male_pismena}")
  return slova_male_pismena,cislice,slova_zacatek_velky,soucet_cislic
    

  



if prihlaseni_do_systemu():
  #print (f"Prihlaseni systemu {vysledek}")
  #zvoleny_text = prace_s_textem()
  #print (f"Zvoleny text {zvoleny_text}")
  #slova = prace_s_textem().split()
  #print (f"Zvoleny text {slova}")
  a,b,c,d = analyza_textu(prace_s_textem())
  print (f"Pocet slov s malymi pismeny {a}")
  print (f"Pocet cislic v textu {b}")
  print (f"Pocet slov zacinajici velkymi pismeny {c}")
  print (f"Pocet slov zacinajici velkymi pismeny {d}")
  


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
      print ("Prihlaseni je neuspesne")
      return False
  except KeyError:
    print ("Zadane uzivatelske jmeno je neplatne")
    return False


#vysledek = prihlaseni_do_systemu()
if prihlaseni_do_systemu:
  print (f"Prihlaseni systemu {prihlaseni_do_systemu()}")
  print (f"Zvoleny text {prace_s_textem()}")
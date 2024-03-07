import random

#zadane_cislo_pocitacem = ""
# zadane_cislo_pocitacem = str(randint(1, 10)) + str(randint(1, 10)) + str(randint(1, 10))+str(randint(1, 10))
#for index in range(0,4):
#    if index == 0:
#        zadane_cislo_pocitacem += str(random.choice(range(1, 10)))
#    else:
        
#        zadane_cislo_pocitacem += str(random.choice(range(1, 10)))

#print(zadane_cislo_pocitacem)

# První číslo z rozsahu 1-9
první = random.choice(range(1, 10))
    
# Zbývající čísla z rozsahu 0-9, vyjma prvního čísla
mozna_cisla = list(range(0, 10))
mozna_cisla.remove(první)
zbyvajici = random.sample(mozna_cisla, 3)
    
# Kombinace prvního čísla se zbyvajícími
cislo = str(první) + ''.join(map(str, zbyvajici))

print(cislo)


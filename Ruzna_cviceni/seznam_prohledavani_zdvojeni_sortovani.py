seznam = ["a","b","a","c","a","d","e","f","g"]
pomocny_seznam = []

"""for znak in seznam:
    
    if znak in pomocny_seznam:
        print("Hodnota je obsažena v pomocnem listu")
        break
    else:
        print("Hodnota neni obsažena")
        pomocny_seznam.append(znak)"""

    

#print("konec prohlidky")

print(seznam)

for i in range(0,len(seznam)):
    #print(seznam[i],sep= "-",end='')
    for j in range(0,len(seznam)):
        #print(seznam[j],sep= "-",end='\n')
        if seznam[i]<seznam[j]:
            seznam[j],seznam[i] = seznam[i],seznam[j]

print(seznam)


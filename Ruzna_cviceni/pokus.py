# Prázdný řetězec, do kterého budeme přidávat znaky
retezec = "Ahoj svete"
novy_list = list(retezec)
# Seznam znaků, které chceme přidat do řetězce
znaky_pridat = ['A', 'h', 'o', 'j', ' ', 's', 'v', 'ě', 't', 'e']
novy_retezec = ""

# Cyklus pro průchod seznamem znaků a jejich přidání do řetězce
for znak in sorted(retezec):
    print(znak)
    novy_retezec += znak

print(novy_retezec)

for i in range(0,len(novy_list)):
    print(novy_list[i])
    novy_list[i+1]=novy_list[i]
    print(novy_list[i])

print(novy_list)



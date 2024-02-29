   
import glob, os, csv
from nptdms import TdmsFile
import numpy as np
from matplotlib import pyplot as plt 
  
  
# Returns a list of names in list files. 
#print("Using glob.glob()") 
#files = glob.glob('C:/Users/MartinFurmanek/Documents/Projekty_Python/Projekt_c2/Data/**/*Results.tdms',  
#                   recursive = True) 
#print("soubory",files)

#for file in files: 
    #print(file) 
  
  
# It returns an iterator which will  
# be printed simultaneously. 
#print("\nUsing glob.iglob()") 
data = []

os.system("cls")

#zadani_od_uzivatele = input("Zadej mi cestu k adresari, kde by meli byt uloženy data: ")
#print("Zadano od uzivatele",zadani_od_uzivatele)
#print("Delka retezce",len(zadani_od_uzivatele))
#print("Pouzity slicing",zadani_od_uzivatele[1:len(zadani_od_uzivatele)-1])
#hodnota_pro_funkci_globe = zadani_od_uzivatele[1:len(zadani_od_uzivatele)-1] + "/**/*Results.tdms"

#print("Hodnota pro funkci Globe",hodnota_pro_funkci_globe)

for filename in glob.iglob("C:/Users/MartinFurmanek/Documents/Projekty_Python/Projekt_c2/**/*Results.tdms", recursive = True): 
    print(filename) 
    #tdms_file = TdmsFile.read(filename)
                      
    # Zde můžeš provést operace se souborem, např. vypsat některé informace
    # Pro tento příklad pouze vypíšeme názvy skupin a kanálů    
    
    with TdmsFile.open(filename) as tdms_file:
        group_name = "Results_Table"
        channel_name = "Jmeno"
        klice = tdms_file[group_name][channel_name][:]
        #print(f"  Aktualni klice: {klice}")
        channel_name = "Hodnota"
        data.append(tdms_file[group_name][channel_name][:])  
        #print(f"  Aktualni data: {data}")


        group = tdms_file[group_name]
        all_groups = tdms_file.groups()
        #print(f"  Group name: {all_groups}")

        channel = group[channel_name]
        all_group_channels = group.channels()
        #print(f"  Channel name: {tdms_file[group_name].channels()}")
        
        #print(f"  Data: {data}")
        #channel = tdms_file[group_name][channel_name]
        #all_channel_data = channel[:]
        #data_subset = channel[1:10]

#print(f"  klicee: {klice}")
#print(f"  \nData: {data}\n")


# Převod seznamu na multidimenzionální numpy pole
data_array = np.array(data)
transponovane_pole = data_array.T

# Kontrola výsledku
print("\n",data_array,"\n")
print("\n",transponovane_pole,"\n")

print("Sloupec pole",data_array[:, 0])
print("Suma sloupce, ", np.sum(data_array[:, 0]))
print("Min sloupce, ", np.min(data_array[:, 0]))
print("Max sloupce, ", np.max(data_array[:, 0]))
print("Mean sloupce, ", np.mean(data_array[:, 0]))


pocet_prvku = len(data_array[0, :])
#print(pocet_prvku)

slovnik = dict()
for klic in klice:   
# Extrahování prvního prvku z každého "listu"
    #for i in range (0,pocet_prvku):
    #    prvek = data_array[:, i]
    #    slovnik[klic] = data_array[:, i]
    slovnik = {klice[i]:data_array[:, i] for i in range(pocet_prvku)}
#       # Výpis výsledku
    #    print("prvek",prvek)
    #    print("polozka slovniku",slovnik[klic])

#print(prvek)


#for klic in klice:
#    print(f"  klic: {klic}")

#for polozka in data:
#    print(f"  polozka v datech: {polozka}")
#    for prvek in polozka:
#        print(f"  prvek v datech: {prvek}")

#print(f"  Data[1]: {data[1]}")

# Vytvoření slovníku z obou seznamů
#slovnik = {klice[i]:[data[0][i], data[1][i]] for i in range(len(klice))}
#slovnik = dict(zip(klice,data))

# Název souboru, do kterého chcete data uložit
nazev_souboru = "data.csv"

# Otevření souboru pro zápis
with open(nazev_souboru, mode='w', newline='', encoding='utf-8') as soubor:
    # Vytvoření CSV zapisovače
    #writer = csv.writer(soubor)
    writer = csv.writer(soubor, delimiter=';')
    # Zápis hlavičky (klíče dictionary jako názvy sloupců)
    writer.writerow(slovnik.keys())
    
    # Zápis dat
    for i in range(len(next(iter(slovnik.values())))):  # iteruje podle délky seznamů v dictionary
        writer.writerow([value[i] for value in slovnik.values()])

    # Výpis vytvořeného slovníku
print("\n",slovnik,"\n") 
print("Prvek slovniku", slovnik['Leakage_locked'])
print("Suma sloupce, ", np.sum(slovnik['Leakage_locked']))
print("Min sloupce, ", np.min(slovnik['Leakage_locked']))
print("Max sloupce, ", np.max(slovnik['Leakage_locked']))
print("Mean sloupce, ", np.mean(slovnik['Leakage_locked']))

#delka_sloupce = pole.shape[0]
#x = np.arange(1,11) 
#y = 

#plt.title("Matplotlib demo") 
#plt.xlabel("x axis caption") 
#plt.ylabel("y axis caption") 
#plt.plot(transponovane_pole[0, :], label=f'Sloupec {0+1}')
#plt.plot(x,y,"ob") 
#plt.show() 

#print(filename)




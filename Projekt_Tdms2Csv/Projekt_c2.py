"""
projekt_c2.py: druhy projekt do Engeto Online Python Akademie
author: Martin Furmanek
email: martin.furmanek@gmail.com
discord: Furmi84
"""

import glob,os
from nptdms import TdmsFile

def prace_se_soubory():
    
    zadani_od_uzivatele = input("Zadej mi cestu k adresari, kde by meli byt uloženy data: ")
    hodnota_pro_funkci_globe = zadani_od_uzivatele[1:len(zadani_od_uzivatele)-1] + "/**/*Results.tdms"    
    cesta_k_datum = glob.glob(hodnota_pro_funkci_globe, recursive = True)
    return cesta_k_datum

def vycteni_data(soubory):
    #(soubory[0])
    data = []    
    for filename in soubory: 
    #print(filename) 
    #tdms_file = TdmsFile.read(filename)
                      
    # Zde můžeš provést operace se souborem, např. vypsat některé informace
    # Pro tento příklad pouze vypíšeme názvy skupin a kanálů    
    
        with TdmsFile.open(filename) as tdms_file:
            
            group_name = "Results_Table"
            channel_name = "Jmeno"
            klic = tdms_file[group_name][channel_name][:]
            #print(f"  Aktualni klic: {klic}")
            channel_name = "Hodnota"
            data.append(tdms_file[group_name][channel_name][:])  
            #print(f"  Aktualni data: {data}")
            print(f"  Channel name: {tdms_file[group_name].channels()}")

    return klic,data



def analyza_dat():
    return 

def export_do_csv():
    return


os.system("cls")
print(f"-"*100)
print(f"\nVítej v aplikaci na prevod dat z TDMS do CSV\n")
print(f"Máš na výběr tyto možnosti:\n")
print ("1.","Načtení data")
print ("2.","Zobrazení dat do grafu")
print ("3.","Zobrazení dat do tabulky")
print ("4.","Analyza data / Určení min,max, std ...")
print ("5.","Export dat do CSV")
print ("6.","Konec aplikace\n")

#volba = int(input("Co si přeješ udělat? "))
#print ("Zvolil sis:", volba)
#match volba:

soubory = prace_se_soubory()

if soubory:
    print(f"  Byli nalezeny dva soubory: {soubory}")
    data = vycteni_data(soubory)
    print(f"  Aktualni data: {data}")
    print("\nData byli nacteny korektně. \n") if data else print("Data nejsou načtena správně")
else:
    print("Nebyl nalezeny žadny soubor s názvem Results.tdms")



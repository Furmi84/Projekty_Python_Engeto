"""
projekt_c2.py: druhy projekt do Engeto Online Python Akademie
author: Martin Furmanek
email: martin.furmanek@gmail.com
discord: Furmi84
"""

import glob
from nptdms import TdmsFile

def prace_se_soubory():
    
    files = glob.glob('C:/Users/MartinFurmanek/Documents/Projekty_Python/Projekt_c2/Data/**/*Results.tdms',  
                   recursive = True) 
    return files

def vycteni_data(soubory):
    return 

def analyza_dat():
    return 

def export_do_csv():
    return

soubory = prace_se_soubory()

print(prace_se_soubory())
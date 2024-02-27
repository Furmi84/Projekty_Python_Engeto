   
import glob 
from nptdms import TdmsFile
  
  
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
for filename in glob.iglob('C:/Users/MartinFurmanek/Documents/Projekty_Python/Projekt_c2/Data/**/*Results.tdms', 
                           recursive = True): 
    #print(filename) 
    #tdms_file = TdmsFile.read(filename)
                      
    # Zde můžeš provést operace se souborem, např. vypsat některé informace
    # Pro tento příklad pouze vypíšeme názvy skupin a kanálů

    data = {}  

    with TdmsFile.open(filename) as tdms_file:
        group_name = "Results_Table"
        channel_name = "Name"
        #data = tdms_file[group_name][channel_name][:]

        group = tdms_file[group_name]
        all_groups = tdms_file.groups()
        #print(f"  Group name: {all_groups}")

        channel = group[channel_name]
        all_group_channels = group.channels()
        #print(f"  Channel name: {all_group_channels}")
        
        #print(f"  Data: {data}")
        channel = tdms_file[group_name][channel_name]
        all_channel_data = channel[:]
        data_subset = channel[1:10]
        
        #print(f"  Data: {all_channel_data}") 
        print(f"  Data Subset: {data_subset}")

        for polozka in data_subset:
            


   
      


    #for group in tdms_file.groups():
        #print(f"  Skupina: {group.name()}")
        #print(f"  Skupina: {group.channels()}")   
        #for channel in group.channels():            
            #print(f"    Kanál: {channel.name}")
            #print(f"    Data: {channel[:]}")
                #Zde můžeš přidat více operací s daty kanálu
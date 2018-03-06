from pathlib import Path
import os

#Python file to practice with putting files in a dictionary with their extension

#User input requested
user_input = input("Voer de master directory in: ")

#Loop die een variabele met het path naar een file update zodat iedere file in de directory wordt afgelopen.
#Vervolgens worden de subdir en de file gejoind in de variabele current_dir
#Hierna wordt een betreffende directory meegegeven aan een splitext commando die de extensie van de file afhaald
for subdir, dirs, files in os.walk(user_input):
    for file in files:
        current_dir = (os.path.join(subdir, file))
        filename, file_extension = os.path.splitext(current_dir)
        print(filename + file_extension)
        print(file_extension)

#Tussen de haakjes moet een path komen die naar een bestand toe leidt. Dit moet dus elke keer geupdate worden.
#De variabele filename wordt dan het path naar het bestand en file_extension wordt de extension.
#filename, file_extension = os.path.splitext()

#Alles uitprinten
#print(filename)
#print(file_extension)

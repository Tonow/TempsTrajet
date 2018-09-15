'''
Fichier:	 python 3
Ecrit par :	 Tonow
Le :		 Date
Sujet:		 TODO
'''

import os
import csv
import google_map_temps
from datetime import datetime

def propose_fichier_csv():
    for file in os.listdir('.'):
        if file.endswith(".csv"):
            print(file)

    ficher_a_traiter = input("\nNom du fichier a traiter : ")
    return ficher_a_traiter


def lire_commune(origCoord, tempsMax , ficher_a_traiter):
    fichierSortie = str(datetime.now()) + ficher_a_traiter[:-4] + origCoord + "_temps_max_" + str(tempsmax)
    firstline = True
    ligneerreur = 'Ligne avec erreur \n'
    print('Traitement')
    with open(ficher_a_traiter, newline='') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row in readCSV:
            if firstline:
                sortie = ', '.join(row)
                print(sortie)
                firstline = False
            destination = row[8]
            print(f"ligne : {readCSV.line_num}")
            if destination != 'Commune acheminement postal':
                try:
                    tempstrajet = google_map_temps.dure_trajet(origCoord, destination)
                    if tempstrajet < tempsMax:
                        tempstrajetmin = int(tempstrajet / 60)
                        print(f"{i} Ville {destination} temps = {tempstrajetmin} min")
                        sortie = sortie + ','.join(row) + '\n'
                except:
                    ligneerreur = ligneerreur + str(i) + ',' + destination + '\n'
                    pass
                i = i+1
            # if i == 25:
            #     break # pour tester
    # print(sortie)
    print('ecriture fichier')
    with open(fichierSortie +'.csv', 'w', newline='') as f:
        f.write(sortie)
    with open('erreur_ligne.csv', 'w', newline='') as f:
        f.write(ligneerreur)

ficher_a_traiter = propose_fichier_csv()

originecoord = input("d'ou penses tu habiter : ")
tempsmax = int(input("le temps max en minute : "))*60 # convertion en seconde

lire_commune(originecoord, tempsmax , ficher_a_traiter)

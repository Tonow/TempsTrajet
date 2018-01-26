'''
Fichier:	 python 3
Ecrit par :	 Tonow
Le :		 Date
Sujet:		 TODO
'''

import csv
import google_map_temps


def lire_commune(origCoord, tempsMax, fichierSortie):
    sortie = 'Id. RCE,NAF,Raison sociale,Enseigne,Tranche effectif (INSEE),Effectif ACOSS (ou recueilli),Adresse principale,Code postal,Commune acheminement postal,'
    ligneerreur = 'Ligne avec erreur \n'
    print('Traitement')
    with open('votre fichier excel.csv', newline='') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row in readCSV:
            destination = row[8]
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
    with open(fichierSortie+'.csv', 'w', newline='') as f:
        f.write(sortie)
    with open('erreur_ligne.csv', 'w', newline='') as f:
        f.write(ligneerreur)


originecoord = input("d'ou penses tu habiter : ")
tempsmax = int(input("le temps max en minute : "))*60 # convertion en seconde
fichiersortie = input("nom du fichier : ")

lire_commune(originecoord, tempsmax, fichiersortie)

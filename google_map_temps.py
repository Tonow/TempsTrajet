'''
Fichier:	 python 3
Ecrit par :	 Tonow
Le :	 Date
Sujet:	 TODO
'''
from datetime import datetime
import googlemaps


def dure_trajet(orig_coord='Bourdeau', dest_coord='paris'):
    '''
        Calcule le temps entre une origine et une destination
    '''
    # orig_coord = input("origine: ")
    # dest_coord = input("destination: ")
    key = 'AIzaSyCG-x6BHrjM1h5vW9BRRLvayIYnHjyKvxc'
    # gmaps = googlemaps.Client(key='AIzaSyAW-3_Xxp6QgNvuqkkVCX4KgoD3EGiGghQ')
    gmaps = googlemaps.Client(key='AIzaSyCG-x6BHrjM1h5vW9BRRLvayIYnHjyKvxc')
    now = datetime.now()
    directions_result = gmaps.directions(orig_coord,
                                         dest_coord,
                                         mode="driving",
                                         avoid="ferries",
                                         departure_time=now
                                        )
    temps_seconde = directions_result[0]['legs'][0]['duration']['value']
    # print(directions_result[0]['legs'][0]['distance']['text'])
    # print(f"temps : {directions_result[0]['legs'][0]['duration']['text']}")
    # print(f"temps value : {temps_seconde}")
    return temps_seconde

import requests
import json
# -*- coding: utf8 -*-
name_f = 'Hola.html'

def get_pokemons(url= 'http://pokeapi.co/api/v2/pokemon-form',offset = 0):
    #offset permite excoger la página
    args = {'offset': offset} if offset else{}
    response = requests.get(url, params=args)

    #Si el status es 200 muestreme lo siguiente
    if response.status_code == 200:
        pyload = response.json()
        results = pyload.get('results',[])

        if results:
            #Recorra los pókemon e imprima los nombres
            for pokemon in results:
                name = pokemon['name']
                print(name)

        #Si quiere imprimir los siguientes 20 vuelva a correr con un ofset mayor
        next = input('Continuar listando {Y/N]')


        if next.upper() == 'Y':
            get_pokemons(offset = offset + 20)
        else:
            print ('Proceso finalizado')
if __name__ == '__main__':
    url = 'http://pokeapi.co/api/v2/pokemon-form'
    get_pokemons()

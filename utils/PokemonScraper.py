from sys import argv
from pygame.constants import TIMER_RESOLUTION
import requests
import shutil
import json
from bs4 import BeautifulSoup
from requests.exceptions import Timeout
from constants import *


def get_all_pokemons():
    url = "https://pokemondb.net/pokedex/all"
    page_response =  requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, 'html.parser')

    pokemon_rows = page_content.find_all('tr')
    pokemon_dict = {}
    for row in pokemon_rows[1:150]:
        html_stats = row.find_all('td')[4:]
        stats_array = list(map(lambda data: int(data.text), html_stats))

        html_types = row.find_all('a', attrs={'class':'type-icon'})
        types_array = list(map(lambda data: TYPES.index(data.text), html_types))

        name = row.find('a', attrs={'class':'ent-name'}).text

        html_mega = row.find('small', attrs={'class':'text-muted'})
        if html_mega:
            name_complete = f"{name}_{html_mega.text}"
        else:
            name_complete = name

        pokemon_id = int(row.find("span", attrs={'class':'infocard-cell-data'}).text)

        pokemon_dict[str(name_complete)] = {
            "ID" : pokemon_id,
            "type1" : types_array[0],
            HP : stats_array[0],
            ATTACK: stats_array[1],
            DEFENSE: stats_array[2],
            SPATTACK: stats_array[3],
            SPDEFENSE: stats_array[4],
            SPEED: stats_array[5],
        }
        if len(types_array) > 1:
            pokemon_dict[name_complete]['type2'] = types_array[1]

        sprites = get_pokemons_sprites(name, pokemon_id)
        pokemon_dict[name_complete]['sprites'] = sprites

    return json.dumps(pokemon_dict)

def get_images(url: str, path:str):
    page_response =  requests.get(url, timeout=5, stream=True)
    with open(path, 'wb') as handle:
        if not page_response.ok:
                print(path ,page_response)
        else:
            handle.write(page_response.content)

def get_pokemons_sprites(pokemon_name: str, pokemon_id : int) -> dict:
    url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
    path = f'resources/sprites/pokemon/{pokemon_name.lower()}_front.png'
    get_images(url, path)
    url_back = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/{pokemon_id}.png"
    path_back = f'resources/sprites/pokemon/{pokemon_name.lower()}_back.png'
    get_images(url_back, path_back)

    return dict(front=path, back=path_back)

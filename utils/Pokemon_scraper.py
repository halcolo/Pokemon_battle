import requests
import json
from bs4 import BeautifulSoup
from requests.exceptions import Timeout
from constants import *


def get_all_pokemons():
    url = "https://pokemondb.net/pokedex/all"
    page_response =  requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, 'html.parser')
    pokemon_data = []

    pokemon_rows = page_content.find_all('tr')
    pokemon_dict = {}
    for row in pokemon_rows[1:]:
        html_stats = row.find_all('td')[4:]
        stats_array = list(map(lambda data: int(data.text), html_stats))

        html_types = row.find_all('a', attrs={'class':'type-icon'})
        types_array = list(map(lambda data: TYPES.index(data.text), html_types))

        name = row.find('a', attrs={'class':'ent-name'}).text

        html_mega = row.find('small', attrs={'class':'text-muted'})
        if html_mega:
            name = f"{name} - {html_mega.text}"

        pokemon_id = row.find("span", attrs={'class':'infocard-cell-data'}).text

        pokemon_dict[str(name)] = {
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
            pokemon_dict[name]['type2'] = types_array[1]

    return json.dumps(pokemon_dict)
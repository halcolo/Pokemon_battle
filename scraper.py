import os
from constants import DIR, ROUTE
from utils.PokemonStats_scraper import get_all_pokemons


if __name__ == "__main__":
    if not os.path.isdir(DIR):
        os.mkdir(DIR)

    json_response = get_all_pokemons()
    
    with open(ROUTE, 'w', encoding='utf-8') as f:
        f.write(json_response)
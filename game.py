import pygame
from pygame.locals import *
from constants import *
from models.Battle import *
from models.Pokemon import *


class Game:
    def __init__(self):
        self.buttons = [500, 500, 100, 40, 'Attack']
        pygame.init()

        self.screen = pygame.display.set_mode((160*4, 144*4))
        pygame.display.set_caption("Pokemon Battle")

        clock = pygame.time.Clock()
        clock.tick(60)

        self.pokemon1 = Pokemon("blastoise", 2, 11, 3)
        self.pokemon2 = Pokemon("rapidash", 2, 9, None)

        self.pokemon1.attacks = [Attack("Spark", 12, SPECIAL, 10, 10, 100)]
        self.pokemon2.attacks = [Attack("Scratch", 0, PHYSICAL, 10, 10, 100)]
        self.loadResources()
        print('Resources Loaded Correctly')


        # Start battle
        self.battle = Battle(self.pokemon1, self.pokemon2)

        self.stopped = False
        print('Initialization finished')


    def loadResources(self):
        self.pokemon1.current_hp = 45
        self.pokemon2.current_hp = 39

        # Stats
        self.pokemon1.basecStats = {
            HP: 0,
            ATTACK: 0,
            DEFENSE: 0,
            SPATTACK: 0,
            SPDEFENSE: 0,
            SPEED: 0
        }

        self.pokemon1.ev = {
            HP: 0,
            ATTACK: 0,
            DEFENSE: 0,
            SPATTACK: 0,
            SPDEFENSE: 0,
            SPEED: 0
        }

        self.pokemon1.iv = {
            HP: 21,
            ATTACK: 21,
            DEFENSE: 21,
            SPATTACK: 21,
            SPDEFENSE: 21,
            SPEED: 21
        }

        self.pokemon1.compute_stats()

        self.pokemon2.basecStats = {
            HP: 0,
            ATTACK: 0,
            DEFENSE: 0,
            SPATTACK: 0,
            SPDEFENSE: 0,
            SPEED: 0
        }

        self.pokemon2.ev = {
            HP: 0,
            ATTACK: 0,
            DEFENSE: 0,
            SPATTACK: 0,
            SPDEFENSE: 0,
            SPEED: 0
        }

        self.pokemon2.iv = {
            HP: 21,
            ATTACK: 21,
            DEFENSE: 21,
            SPATTACK: 21,
            SPDEFENSE: 21,
            SPEED: 21
        }

        self.pokemon2.compute_stats()

        self.loadPokemonImage(self.pokemon1, True)
        self.loadPokemonImage(self.pokemon2, False)


    def loadPokemonImage(self, pokemon, is_player):
        pokemon_name = pokemon.name.lower()
        if is_player:
            pokemon_img = pygame.image.load(f'resources/sprites/pokemon/{pokemon.name}_back.png')
            pokemon_img = pygame.transform.scale(pokemon_img, (400,400))
            pokemon.renderer = (pokemon_img)
        else:
            pokemon_img = pygame.image.load(f'resources/sprites/pokemon/{pokemon.name}_front.png')
            pokemon_img = pygame.transform.scale(pokemon_img, (400,400))
            pokemon.renderer = (pokemon_img)

    def renderPokemons(self):
        self.pokemon1.render(self.screen, (0, 200))
        self.pokemon2.render(self.screen, (400, 0))

    def exit_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopped = True


        self.update()
        self.render()

    def update(self):
        pass

    def render(self):
        self.screen.fill((255, 255, 255))
        self.renderPokemons()
        pygame.display.update()


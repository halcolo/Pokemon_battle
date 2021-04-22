import pygame
from pygame.display import update
from pygame.locals import *
from constants import *
from models.Pokemon import *
from models.Battle import * 
from game import Game


if __name__ == "__main__":

    game = Game()
    while not game.stopped:
        game.process()
        game.render()
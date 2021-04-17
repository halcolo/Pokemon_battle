import pygame
from pygame.display import update
from pygame.locals import *
from constants import *
from models.Pokemon import *
from models.Battle import * 
from game import Game


def ask_command(pokemon):
    command = None
    while not command:
        # DO ATTACK  -> attack 0
        tmp_command = input(f"What should {pokemon.name} do?: ").split(" ")
        if  len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command

"""
while not battle.is_finished():
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        # Execute turn
        battle.execute_turn(turn)
        battle.print_current_status()
"""


if __name__ == "__main__":

    game = Game()
    while not game.stopped:
        game.exit_input()
        game.update()
        game.render()
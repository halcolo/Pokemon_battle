from constants import *
from models.Pokemon import *
from models.Battle import * 

# First define pokemons with their stats

pokemon1 = Pokemon("Bulbasaur", 78, TYPES[11], TYPES[4])
pokemon2 = Pokemon("Charmander", 68, TYPES[9], None)
pokemon1.current_hp = 45
pokemon2.current_hp = 39

# Stats

pokemon1.basecStats = {
    HP: 108,
    ATTACK: 130,
    DEFENSE: 95,
    SPATTACK: 80,
    SPDEFENSE: 85,
    SPEED: 102
}

pokemon1.iv = {
    HP: 24,
    ATTACK: 12,
    DEFENSE: 30,
    SPATTACK: 16,
    SPDEFENSE: 23,
    SPEED: 5
}

pokemon1.ev = {
    HP: 74,
    ATTACK: 190,
    DEFENSE: 91,
    SPATTACK: 48,
    SPDEFENSE: 84,
    SPEED: 23
}

pokemon1.compute_stats()
print(pokemon1.stats)

pokemon2.basicStats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

pokemon2.iv = {
    HP: 24,
    ATTACK: 12,
    DEFENSE: 30,
    SPATTACK: 16,
    SPDEFENSE: 23,
    SPEED: 5
}

pokemon2.ev = {
    HP: 74,
    ATTACK: 190,
    DEFENSE: 91,
    SPATTACK: 48,
    SPDEFENSE: 84,
    SPEED: 23
}

# Attacks

scratch = Attack("scratch", "normal", PHYSICAL, 10, 10, 100)
pokemon1.attacks = [scratch]
pokemon2.attacks = [scratch]

# Start battle

battle = Battle(pokemon1, pokemon2)

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
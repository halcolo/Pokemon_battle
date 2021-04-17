from constants import *

class Pokemon:
    def __init__ (self, name:str, level:int,
                type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = []
        self.stats = {}
        self.basecStats = {}
        self.ev = {}
        self.iv = {}
        self.current_status = 0
        self.current_hp = 0
        self.nature = 0
        self.renderer = None

    def render(self, screen, position):
        if self.renderer:
            print('rendering')
            screen.blit(self.renderer, position)

    def compute_stats(self):
        self.stats = {
            HP: self.compute_hp_stat(),
            ATTACK: self.compute_standart_stats(ATTACK),
            DEFENSE: self.compute_standart_stats(DEFENSE),
            SPATTACK: self.compute_standart_stats(SPATTACK),
            SPDEFENSE: self.compute_standart_stats(SPDEFENSE),
            SPEED: self.compute_standart_stats(SPEED)
        }

    def compute_standart_stats(self, stat):
        value1 = (2 * self.basecStats[stat] + self.iv[stat] + int(self.ev[stat]/4)) * self.level
        return ((int(value1 /100)) + 5) * NATURE_MATRIX[self.nature][stat]

    def compute_hp_stat(self):
        value1 = (2 * self.basecStats[HP] + self.iv[HP] + int(self.ev[HP]/4)) * self.level
        return (value1 /100) + self.level + 10

class Attack:
    def __init__ (self, name, attack_type, category, pp, power, accuracy):
        self.name = name
        self.type = attack_type
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
 
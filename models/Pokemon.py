from constants import *

class Pokemon:
    def __init__ (self, name:str, level:int,
                type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = []
        self.basicStats = {}
        self.current_status = 0
        self.current_hp = 0


class Attack:
    def __init__ (self, name, attack_type, category, pp, power, accuracy):
        self.name = name
        self.type = attack_type
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
 
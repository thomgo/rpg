# coding: utf-8
import random

class Character():
    def __init__(self, life, attack, defense, agility, name = False):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.agility = agility

    def attacks(self, target):
        print("{} attaque violemment {}".format(self.name, target.name))
        if random.randrange(0,100) <= target.agility:
            print("{} a esquivé l'attaque".format(target.name))
            return False
        target.life -= self.attack - (target.defense/5)
        print("{} a maintenant {} de vie".format(target.name, target.life))

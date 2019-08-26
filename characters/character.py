# coding: utf-8
import random

class Character():
    """Mother class with base caractestics of the different characters
    class attribut: actions
    attributs: name, life, attack, defense, agility
    methods: attacks, escape
    """
    actions = {
        'a': 'attaquer',
        'f': 'fuir'
    }

    def __init__(self, life, attack, defense, agility, name = False):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.agility = agility

    def attacks(self, target):
        """Function to make the character attack an other one.
        If the target can not avoid the attack, it looses life
        """
        print("{} attaque violemment {}".format(self.name, target.name))
        # Offer a chance to the target to avoid the attack
        # Exemple: a character with 50 in agility has 1/2 chances to avoid the attack
        if random.randrange(0,100) <= target.agility:
            print("{} a esquivé l'attaque".format(target.name))
            return False
        # Substract to target's life the character's attack minus the target defens divided by 5
        target.life -= self.attack - (target.defense/5)
        print("{} a maintenant {} de vie".format(target.name, target.life))

    def escape(self):
        """Function to allow the character to try to escape and leave the fight"""
        # Lower the chance to escape according to the character's agility
        agi = round(self.agility/5)
        if random.randrange(0,100) <= agi:
            return True
        return False

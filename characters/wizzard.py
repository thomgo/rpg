#coding: utf-8

from .character import Character

class Wizzard(Character):
    """Class representing a wizzard character.
    Attributs: mana
    methods = heal, str"""
    actions: Character.actions.update({'s': 'se soigner'})

    def __init__(self, name = False):
        super().__init__(600, 20, 50, 25, name)
        # Represents the magical power
        self.mana = 200

    def heal(self):
        """Function to increase the life of the wizzard with the mana power"""
        # The spell requires at least 50 points of mana
        if self.mana >= 50:
            print("{} lance un puissant sort de soin".format(self.name))
            self.mana -= 50
            self.life += 20
            print("{} regagne 20 points de vie, santé actuelle : {}".format(self.name, self.life))
        else :
            print("{} tente de puiser en lui les forces nécessaires pour se soigner mais son mana n'est pas suffisant".format(self.name))

    def __str__(self):
        return "{} : vie = {}, mana = {}".format(self.name, self.life, self.mana)

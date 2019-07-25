# coding: utf-8

class Factory():
    @classmethod
    def get_character(self, class_name):
        if class_name == "warrior":
            from characters.warrior import Warrior
            return Warrior()
        elif class_name == "archer":
            from characters.archer import Archer
            return Archer()
        else:
            from characters.wizzard import Wizzard
            return Wizzard()

    @classmethod
    def get_ennemy(self, class_name):
        if class_name == "orc":
            from characters.orc import Orc
            return Orc("Gentro")
        elif class_name == "wolf":
            from characters.wolf import Wolf
            return Wolf("Radak")
        else:
            from characters.zombie import Zombie
            return Zombie("Sillion")

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

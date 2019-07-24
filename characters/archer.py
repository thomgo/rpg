#coding: utf-8

from characters.character import Character

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 350, 80, 30, 50)

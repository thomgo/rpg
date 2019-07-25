#coding: utf-8

from characters.character import Character

class Archer(Character):
    def __init__(self, name = False):
        super().__init__(350, 80, 30, 50, name)

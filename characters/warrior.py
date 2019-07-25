#coding: utf-8

from characters.character import Character

class Warrior(Character):
    def __init__(self, name = False):
        super().__init__(500, 50, 80, 10, name)

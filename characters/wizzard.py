#coding: utf-8

from characters.character import Character

class Wizzard(Character):
    def __init__(self, name):
        super().__init__(name, 600, 20, 50, 25)

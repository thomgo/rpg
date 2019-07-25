#coding: utf-8

from characters.character import Character

class Orc(Character):
    def __init__(self, name = False):
        super().__init__(400, 40, 70, 20, name)

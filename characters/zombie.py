#coding: utf-8

from characters.character import Character

class Zombie(Character):
    def __init__(self, name = False):
        super().__init__(600, 15, 15, 5, name)

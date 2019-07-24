#coding: utf-8

from characters.character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 500, 50, 80, 10)

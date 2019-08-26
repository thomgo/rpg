#coding: utf-8

from characters.character import Character

class Orc(Character):
    """Class representing an orc character"""
    def __init__(self, name = False):
        super().__init__(400, 40, 70, 20, name)

#coding: utf-8

from characters.character import Character

class Wolf(Character):
    """Class representing a wolf character"""
    def __init__(self, name = False):
        super().__init__(300, 30, 15, 40, name)

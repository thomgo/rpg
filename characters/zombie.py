#coding: utf-8

from .character import Character

class Zombie(Character):
    """Class representing a zombie character"""
    def __init__(self, name = False):
        super().__init__(600, 15, 15, 5, name)

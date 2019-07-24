# coding: utf-8

from game.narrator import Narrator
from characters.warrior import Warrior

if __name__ == '__main__':
    player = Warrior("Thor")
    narrator = Narrator()
    narrator.introduction()
    narrator.choose_character()
    

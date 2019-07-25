# coding: utf-8

from game.narrator import Narrator
from game.factory import Factory

if __name__ == '__main__':
    narrator = Narrator()

    narrator.introduction()
    choice = narrator.choose_character()
    player = Factory.get_character(choice)
    narrator.player_customization(player)
    

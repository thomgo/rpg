# coding: utf-8

from game.narrator import Narrator
from game.factory import Factory
from game.arena import Arena

if __name__ == '__main__':
    narrator = Narrator()
    arena = Arena()


    narrator.introduction()
    choice = narrator.choose_character()
    player = Factory.get_character(choice)
    narrator.player_customization(player)
    ennemy = Factory.get_ennemy('orc')

    story = [
        'Votre voyage commence. Vous marchez au bord des imposantes montagne de la Moria',
        'Le soleil est chaud sur votre visage et la neige fraîche à vos pieds',
        'Vous entendez alors un bruissement sourd, vous vous retournez',
        'Vous êtes alors nez à nez avec un orc qui vous attaque',
    ]
    narrator.tell(story)

    arena.fighters_enter(player, ennemy)
    arena.battle()

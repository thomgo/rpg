# coding: utf-8

from game.narrator import Narrator
from game.factory import Factory

if __name__ == '__main__':
    narrator = Narrator()

    narrator.introduction()
    choice = narrator.choose_character()
    player = Factory.get_character(choice)
    narrator.player_customization(player)
    ennemy = Factory.get_ennemy('orc')

    print('Votre voyage commence. Vous marcher au bord des imposantes montagne de la Moria\n\
Le soleil est chaud sur votre visage et la neige fraîche à vos pieds\n\
Vous entendez alors un bruissement sourd, vous vous retournez\n\
Vous êtes alors nez à nez avec un orc qui vous attaque')

    print('Vous entrez en combat avec {}'.format(ennemy.name))

    while player.life > 0 and ennemy.life > 0:
        player.attacks(ennemy)
        ennemy.attacks(player)

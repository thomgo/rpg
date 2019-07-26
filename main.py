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

    story = [
        'Votre voyage commence. Vous marcher au bord des imposantes montagne de la Moria',
        'Le soleil est chaud sur votre visage et la neige fraîche à vos pieds',
        'Vous entendez alors un bruissement sourd, vous vous retournez',
        'Vous êtes alors nez à nez avec un orc qui vous attaque',
    ]
    narrator.tell(story)

    while player.life > 0 and ennemy.life > 0:
        action = input('Que souhaitez-vous faire (a=attaquer, f=fuir) ? : ').lower()
        if action == 'a':
            player.attacks(ennemy)
        elif action == 'f':
            if player.escape():
                print("Vous réussissez à fuir au dernier moment dans un élan d'agilité")
                break
            else:
                print('Votre ennemi vous rattrape !')
        ennemy.attacks(player)

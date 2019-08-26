# coding: utf-8

from game.narrator import Narrator
from game.factory import Factory
from game.arena import Arena

if __name__ == '__main__':
    # Start a narrator to tell the story
    narrator = Narrator()
    # Start an arena where battles are going to take place
    arena = Arena()

    introduction = [
        "Bienvenue aventurier aux portes d'un nouveau monde de magie et de légendes.",
        "Ici commence ton histoire, laisse toi guider par le narrateur de ce monde.",
        "Ta légende raisonnera pour des siècles et des siècles"
    ]
    narrator.tell(introduction)
    # Allow the user to choose his type of character and retrieve it from the factory
    choice = narrator.choose_character()
    player = Factory.get_character(choice)
    narrator.player_customization(player)
    # Retrieve an ennemy from factory, for this scenario an orc
    ennemy = Factory.get_character('orc')
    ennemy.name = 'Gentro'

    # Exemple story to be told by the narrator
    story = [
        'Votre voyage commence. Vous marchez au bord des imposantes montagne de la Moria',
        'Le soleil est chaud sur votre visage et la neige fraîche à vos pieds',
        'Vous entendez alors un bruissement sourd, vous vous retournez',
        'Vous êtes alors nez à nez avec un orc qui vous attaque',
    ]
    narrator.tell(story)

    # Start a fight
    arena.fighters_enter(player, ennemy)
    arena.battle()

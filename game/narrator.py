# coding: utf-8

from game.storyAgent import storyAgent

class Narrator(storyAgent):
    """ Class to tell the story and interact with the player.
    class attributs: allowed roles with their translation
    attributs: none
    methods: introduction, tell, choose_character, player_customization
    """

    roles = {
        "guerrier" : "warrior",
        "archer" : "archer",
        "magicien" : "wizzard"
    }

    def __init__(self):
        pass

    def introduction(self):
        """Function to introduct the game by a little text with transition"""
        self.transition(2)
        print("""Bienvenue aventurier aux portes d'un nouveau monde de magie et de légendes
Ici commence ton histoire, laisse toi guider par le narrateur de ce monde.
Ta légende raisonnera pour des siècles et des siècles""")

    def tell(self, story):
        """Function to display with a transition each sentence of a given list"""
        for sentence in story:
            self.transition(3)
            print(sentence)

    def choose_character(self):
        """Function to allow the player to choose a character type from the roles
        While the player does not choose an existant role the function runs a while loop
        """
        self.transition(7)
        print("""Avant de commencer ton aventure, qui veux tu incarner ?
- Un guerrier fort et solide comme la pierre
- Un archer agile et souple comme le vent
- Un magicien intelligent et rusé comme le corbeau""")
        while True:
            try:
                player_choice = input('Je veux incarner un : ').lower()
                # Check if player_choice is in the roles class attribut
                player_class = Narrator.roles[player_choice]
                break
            except:
                print('Je ne reconnais pas ce personnage')
        return player_class

    def player_customization(self, player):
        """Function to allow the player to choose a character name"""
        self.transition(2)
        name = input("Quel est votre nom aventurier ? : ")
        player.name = name

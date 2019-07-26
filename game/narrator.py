# coding: utf-8
import os
import time

class Narrator():
    roles = {
        "guerrier" : "warrior",
        "archer" : "archer",
        "magicien" : "wizzard"
    }

    def __init__(self):
        pass

    def transition(self, waiting_time):
        """Function to make a break and clear the screen"""
        time.sleep(waiting_time)
        os.system('cls||clear')

    def introduction(self):
        self.transition(2)
        print("""Bienvenue aventurier aux portes d'un nouveau monde de magie et de légendes
Ici commence ton histoire, laisse toi guider par le narrateur de ce monde.
Ta légende raisonnera pour des siècles et des siècles""")

    def choose_character(self):
        self.transition(7)
        print("""Avant de commencer ton aventure, qui veux tu incarner ?
- Un guerrier fort et solide comme la pierre
- Un archer agile et souple comme le vent
- Un magicien intelligent et rusé comme le corbeau""")
        while True:
            try:
                player_choice = input('Je veux incarner un : ').lower()
                player_class = Narrator.roles[player_choice]
                break
            except:
                print('Je ne reconnais pas ce personnage')

        return player_class

    def player_customization(self, player):
        self.transition(2)
        name = input("Quel est votre nom aventurier ? : ")
        player.name = name

    def tell(self, story):
        for sentence in story:
            self.transition(3)
            print(sentence)

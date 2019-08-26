# coding: utf-8

from game.storyAgent import storyAgent

class Arena(storyAgent):
    """Class to represent a battlefield during the story and manage the fights
    attributs : player, ennemy
    methods: fighters_enter, fighters_leave, battle
    """

    def __init__(self):
        # Both attributs expect characters objects
        self.player = False
        self.ennemy = False

    def fighters_enter(self, player, ennemy):
        """Function to store characters objects in player and ennemy attributs"""
        self.player = player
        self.ennemy = ennemy

    def fighters_leave(self):
        """Function to clear player and ennemy attributs"""
        self.player = False
        self.ennemy = False

    def battle(self):
        """function to ask player for an action and execute it while bot player or ennemy are alive"""
        self.transition(2)
        while self.player.life > 0 and self.ennemy.life > 0:
            while True:
                action = input('Que souhaitez-vous faire {} ? : '.format(self.player.actions)).lower()
                if action in self.player.actions:
                    break
                print('Action impossible')
            if action == 'a':
                self.player.attacks(self.ennemy)
            elif action == 'f':
                if self.player.escape():
                    print("Vous réussissez à fuir au dernier moment dans un élan d'agilité")
                    break
                else:
                    print('Votre ennemi vous rattrape !')
            elif action == 's':
                self.player.heal()
            self.ennemy.attacks(self.player)
            self.transition(3)
        print('Le combat prend fin')
        self.fighters_leave()

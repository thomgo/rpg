# coding: utf-8

from .storyAgent import storyAgent

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
        """function to ask player for an action and execute it while both player or ennemy are alive"""
        self.transition(2)
        # As long both characters are alive
        while self.player.life > 0 and self.ennemy.life > 0:
            try:
                action_is_allowed = False
                # check if the character can make the action and execute it
                while not action_is_allowed:
                    print("{} || {}".format(self.player, self.ennemy))
                    action = input('Que souhaitez-vous faire {} ? : '.format(self.player.actions)).lower()
                    action_is_allowed = self.player.make_action(action, self.ennemy)
            # If the character succeed to escape
            except Exception as e:
                break
            # Ennemie's turn, if not dead
            if self.ennemy.life > 0:
                self.ennemy.attacks(self.player)
            self.transition(5)
        # End of the fight
        print('Le combat prend fin')
        self.fighters_leave()

#coding: utf-8

import os
import time

class storyAgent():
    """ Mother class to all the objects that make the story living like the narrator or the arena
    attributs : none
    methods : transition
    """
    def __init__(self):
        pass

    def transition(self, waiting_time):
        """Function to make a break and clear the screen"""
        time.sleep(waiting_time)
        os.system('cls||clear')

#coding: utf-8

import os
import time

class storyAgent():
    def __init__(self):
        pass

    def transition(self, waiting_time):
        """Function to make a break and clear the screen"""
        time.sleep(waiting_time)
        os.system('cls||clear')

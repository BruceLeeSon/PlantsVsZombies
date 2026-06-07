import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Зеленский vs ZOVbies"

class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)



window = Game()

arcade.run()
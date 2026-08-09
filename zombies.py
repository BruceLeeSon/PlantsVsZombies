import arcade
from pyglet.sprite import Sprite

import animate
from constants import SCREEN_WIDTH


class Zombie(animate.Animate):
    def __init__(self, image, health, row, center_y):
        super().__init__(image, 0.09)
        self.health = health
        self.row = row
        self.set_position(SCREEN_WIDTH, center_y)
        self.change_x = 0.2

    def update(self):
        self.center_x -= self.change_x
        if self.health <= 0:
            self.kill()

class SimpleZombie(Zombie):
    def __init__(self, row, center_y):
        super().__init__("zombies/OrdinaryZombie/Zombie_0.png", 12, row, center_y)
        for zombies in range(22):
            self.append_texture(arcade.load_texture(f"zombies/OrdinaryZombie/Zombie_{zombies}.png"))
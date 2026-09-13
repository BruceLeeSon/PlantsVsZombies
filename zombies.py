import arcade
from pyglet.sprite import Sprite

import animate
from constants import SCREEN_WIDTH


class Zombie(animate.Animate):
    def __init__(self, image, health, row, center_y, window):
        super().__init__(image, 0.8)
        self.health = health
        self.row = row
        self.set_position(SCREEN_WIDTH, center_y + 15)
        self.change_x = 0.2
        self.eating = False
        self.window = window




    def update(self):
        if not self.eating:
            self.center_x -= self.change_x

        if self.health <= 0:
            self.kill()

        self.eating = False
        food = arcade.check_for_collision_with_list(self, self.window.plants)
        for plant in food:
            if self.row == plant.row:
                self.eating = True
                plant.health -= 0.5
                print(plant.health, plant.row, plant.column)



class SimpleZombie(Zombie):
    def __init__(self, row, center_y, window):
        super().__init__("zombies/OrdinaryZombie/Zombie_0.png", 12, row, center_y, window)
        for zombies in range(22):
            self.append_texture(arcade.load_texture(f"zombies/OrdinaryZombie/Zombie_{zombies}.png"))


class ConeHeadZombie(Zombie):
    def __init__(self, row, center_y, window):
        super().__init__("zombies/ConeheadZombie/ConeheadZombie_0.png", 20, row, center_y, window)
        for czombies in range(21):
            self.append_texture(arcade.load_texture(f"zombies/ConeheadZombie/ConeheadZombie_{czombies}.png"))
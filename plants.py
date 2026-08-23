import arcade
from arcade import check_for_collision_with_list

import animate
import time
import sun
import zombies
from constants import SCREEN_WIDTH


class Plant(animate.Animate):
    def __init__(self, image, health, cost):
        super().__init__(image, 0.12)

        self.health = health
        self.cost = cost

        self.row = 0
        self.column = 0

    def update(self):
        if self.health <= 0:
            self.kill()

    def planting(self, center_x, center_y, row, column):
        self.set_position(center_x, center_y)
        self.row = row
        self.column = column


class Sunflower(Plant):
    def __init__(self, window):
        super().__init__("plants/sun1.png", 80, 50)
        self.append_texture(arcade.load_texture("plants/sun1.png"))
        self.append_texture(arcade.load_texture("plants/sun2.png"))

        self.sun_spawn_time = time.time()

        self.window = window

    def update(self):
        if time.time() - self.sun_spawn_time >= 15:
            new_sun = sun.Sun(self.right, self.top)
            self.sun_spawn_time = time.time()
            self.window.suns.append(new_sun)

        self.window.suns.update()

class PeaShooter(Plant):
    def __init__(self, window):
        super().__init__("plants/pea1.png", health=100, cost=100)
        self.pea_spawntime = time.time()
        self.window = window

        for i in range(3):
            self.append_texture(arcade.load_texture(f"plants/pea{i+1}.png"))

    def update(self):
        zombie_on_line = False

        for zombie in self.window.zombies:
            if zombie.row == self.row:
                zombie_on_line = True
                break

        if time.time() - self.pea_spawntime >= 2 and zombie_on_line:
            new_pea = Pea(self.right, self.top - 15, self.window)
            self.pea_spawntime = time.time()

            self.window.peas.append(new_pea)

class Pea(arcade.Sprite):
    def __init__(self, center_x, center_y, window):
        super().__init__("items/bul.png", 0.12)
        self.set_position(center_x, center_y)
        self.change_x = 7
        self.damage = 1
        self.window = window

    def update(self):
        self.center_x += self.change_x
        if self.center_x > SCREEN_WIDTH:
            self.kill()
        zombies = check_for_collision_with_list(self, self.window.zombies)
        for zombie in zombies:
            zombie.health -= self.damage
            self.kill()
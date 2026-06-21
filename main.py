import arcade
import random


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Plants vs Zombies"

class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.bg = arcade.load_texture("textures/background.jpg")
        self.menu = arcade.load_texture("textures/menu_vertical.png")



    def setup(self):
        pass

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        arcade.draw_texture_rectangle(67, SCREEN_HEIGHT / 2, 134, SCREEN_HEIGHT, self.menu)

    def update(self, delta_time):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # print(x,y)
        if 16 <= x <= 116:
            print(y)
            if 370 <= y <= 480:
                print("#1")

            if 255 <= y <= 365:
                print("#2")

            if 140 <= y <= 250:
                print("#3")

            if 25 <= y <= 135:
                print("#4")
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        pass




window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

window.setup()

arcade.run()
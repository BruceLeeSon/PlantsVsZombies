import arcade
import random
import plants

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Plants vs Zombies"

CELL_WIDTH = 78
CELL_HEIGHT = 100


def lawn_x(x):
    right_x = 248 + CELL_WIDTH
    column = 1
    while right_x <= x:
        right_x += CELL_WIDTH
        column += 1

    center_x = right_x - CELL_WIDTH / 2
    return center_x, column


def lawn_y(y):
    up_y = 24 + CELL_HEIGHT
    lane = 1
    while up_y <= y:
        up_y += CELL_HEIGHT
        lane += 1

    center_y = up_y - CELL_HEIGHT / 2
    return center_y, lane


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.bg = arcade.load_texture("textures/background.jpg")
        self.menu = arcade.load_texture("textures/menu_vertical.png")

        self.plants = arcade.SpriteList()
        self.suns = arcade.SpriteList()

        self.seed = None
        self.lawns = []
        self.sun = 300

        self.seed_sound = arcade.load_sound("sounds/seed.mp3")

    def setup(self):
        pass

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        arcade.draw_texture_rectangle(67, SCREEN_HEIGHT / 2, 134, SCREEN_HEIGHT, self.menu)

        self.plants.draw()
        self.suns.draw()

        if self.seed is not None:
            self.seed.draw()

        arcade.draw_text(str(self.sun), 34, 490, (165, 42, 42), 30)

    def update(self, delta_time):
        self.plants.update()
        self.plants.update_animation(delta_time)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)
        if 16 <= x <= 116:
            print(y)
            if 370 <= y <= 480:
                print("Sunflower")
                self.seed = plants.Sunflower(self)

            if 255 <= y <= 365:
                print("Wallnut")

            if 140 <= y <= 250:
                print("#3")

            if 25 <= y <= 135:
                print("#4")

            if self.seed is not None:
                self.seed.center_x = x
                self.seed.center_y = y
                self.seed.alpha = 150

        for sun in self.suns:
            if sun.left <= x <= sun.right and sun.bottom <= y <= sun.top:
                sun.kill()
                self.sun += 25

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.seed is not None:
            self.seed.center_x = x
            self.seed.center_y = y

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if 248 <= x <= 950 and 24 <= y <= 524 and self.seed is not None:
            center_x, column = lawn_x(x)
            center_y, lane = lawn_y(y)

            if (lane, column) in self.lawns or self.sun < self.seed.cost:
                self.seed = None
                return

            self.lawns.append((lane, column))
            print(self.lawns)

            self.sun -= self.seed.cost
            self.seed.planting(center_x, center_y, lane, column)
            self.seed.alpha = 255
            self.plants.append(self.seed)
            self.seed = None

            arcade.play_sound(self.seed_sound)
        else:
            self.seed = None


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

window.setup()

arcade.run()

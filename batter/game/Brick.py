import raylibpy
from game.point import Point
from game import constants
from game.actor import Actor

class Brick(Actor):

    def __init__(self, x, y):

        super().__init__()

        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)
        position = Point(x,y)
        self.set_position(position)
        self.set_image(constants.IMAGE_BRICK)

    def set_position(self, position):
        return super().set_position(position)

    def get_position(self):
        return super().get_position()
        


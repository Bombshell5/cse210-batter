import raylibpy
from batter.game import point
from game import constants
from game.actor import Actor

class Brick(Actor):
    def __init__(self, x, y):
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)
        position = point(x,y)
        self.set_position(position)
        



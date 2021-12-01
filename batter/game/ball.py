from game.actor import Actor
from game.point import Point
from game import constants

class Ball(Actor):
    def __init__(self, x, y):

        super().__init__()

        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)
        position = Point(x,y)
        self.set_position(position)
        self.set_image(constants.IMAGE_BALL)
        self.set_velocity(Point(10,10))


    def set_position(self, position):
        return super().set_position(position)

    def get_position(self):
        return super().get_position()
    

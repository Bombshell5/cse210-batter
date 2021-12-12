from game.action import Action
from game.point import Point
from game.physics_service import PhysicsService
from game import constants

class HandleOffScreenAction(Action):
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, cast):
        ball = cast["balls"][0]
        postion = self.get_position()
        x = postion.get_x()
        y = postion.get_y()
        if(x > constants.X_MAX):
            new_x = x - 10
        if (y > constants.Y_MAX):
            new_y = y - 10
        
            




        
    
        
        
        



from constants import *
from game.scripting.action import Action


class ControlShootAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        shoot = cast.get_first_actor(SHOOT_GROUP)
        if self._keyboard_service.is_key_down(SPACE): 
            shoot.move_left()
        elif self._keyboard_service.is_key_down(SPACE): 
            shoot.move_right()  
        else: 
            shoot.stop_moving()        
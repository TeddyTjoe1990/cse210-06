from email.quoprimime import body_check
from turtle import position
from game.casting.actor import Actor

class Enemy(Actor):
    """Enemies that can be shoot."""

    def __init__(self, body, animation, points, debug=False):
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
    
    def get_animation(self): 
        """Gets the enemy's image."""
        return self._animation

    def get_body(self):
        """Gets the enemies body."""
        return self._body

    def move_next(self):
        """Moves the enemies using its velocity"""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_down(self):
        """Moves the enemies down."""
        x = self._position.get_x
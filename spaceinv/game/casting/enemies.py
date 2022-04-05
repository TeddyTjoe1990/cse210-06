
from game.casting.actor import Actor

class Enemy(Actor):
    """Enemies that can be shoot."""

    def __init__(self, body, image, points, debug=False):
        super().__init__(debug)
        self._body = body
        self._image = image
        self._points = points
    
    def get_image(self): 
        """Gets the enemy's image."""
        return self._image

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

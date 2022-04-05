
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Shoot(Actor):
    """An implement to shoot from the ship."""
    def __init__(self, body, image, debug=False):
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_image(self):
        """Gets the shoot's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the shoot's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
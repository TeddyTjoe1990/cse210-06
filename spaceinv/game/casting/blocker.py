
from spaceinv.game.casting.actor import Actor


class Blocker():
    def __init__(self, size, color, row, column):
        self.height = size
        self.width = size
        self.color = color
        #self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self, keys, *args):
        #game.screen.blit(self.image, self.rect)
        pass
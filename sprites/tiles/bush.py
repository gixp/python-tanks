import pygame
from units.visual import Visual


class Bush(Visual):

    def __init__(self, position, sprites):
        super().__init__(
            position = position, 
            path = 'assets/bush.png', 
            groups = [sprites['visible']]
        )
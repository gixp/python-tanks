import pygame
from units.visual import Visual


class Ground(Visual):

    def __init__(self, position, sprites):
        super().__init__(
            position = position, 
            path = 'assets/ground.png', 
            groups = [sprites['visible']]
        )
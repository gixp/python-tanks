import pygame
from units.tile import Tile


class Box1(Tile):

    def __init__(self, position, sprites):
        super().__init__(
            position = position, 
            hp = 60,
            path = 'assets/box1.png', 
            groups = [sprites['visible'], sprites['obstacle']]
        )
        self.paths_hit = ['assets/box1_hit1.png']
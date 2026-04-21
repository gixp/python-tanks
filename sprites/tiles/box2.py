import pygame
from units.tile import Tile


class Box2(Tile):

    def __init__(self, position, sprites):
        super().__init__(
            position = position, 
            hp = 90,
            path = 'assets/box2.png', 
            groups = [sprites['visible'], sprites['obstacle']]
        )
        self.paths_hit = ['assets/box2_hit1.png', 'assets/box2_hit2.png']
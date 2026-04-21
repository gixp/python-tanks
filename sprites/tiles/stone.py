import pygame
from units.tile import Tile


class Stone(Tile):

    def __init__(self, position, sprites):
        super().__init__(
            position = position, 
            hp = 500,
            path = 'assets/stone.png', 
            groups = [sprites['visible'], sprites['obstacle']]
        )
import pygame
from units.boost import Boost



class Ammunition(Boost):
    
    def __init__(self, position, sprites):
        super().__init__(
            position = position, 
            path = 'assets/ammunition.png', 
            groups = [sprites['visible'], sprites['boost']], 
            objects = sprites['object'],
            attribute = 'ammunition', 
            amount = 3
        )
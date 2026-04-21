import pygame
from units.boost import Boost



class Heal(Boost):
    
    def __init__(self, position, sprites):
        super().__init__(
            position = position, 
            path = 'assets/heal.png', 
            groups = [sprites['visible'], sprites['boost']], 
            objects = sprites['object'],
            attribute = 'hp', 
            amount = 50
        )
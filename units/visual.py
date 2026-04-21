import pygame
from units.sprite import Sprite


class Visual(Sprite):

    def __init__(self, position, path, groups):
        super().__init__(position, path, groups)
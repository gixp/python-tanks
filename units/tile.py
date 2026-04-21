import pygame
from units.obstacle import Obstacle


class Tile(Obstacle):
    def __init__(self, position, path, groups, hp):
        super().__init__(position, path, groups, hp)

    def _hit_action(self):
        if hasattr(self, 'paths_hit'):
            path_id = self.hit_counter - 1
            path = self.paths_hit[path_id]
            self._set_image(path)
import pygame
from units.obstacle import Obstacle


class Moving(Obstacle):

    def __init__(self, position, path, groups, hp, speed, obstacles, vector=(0, 0)):
        super().__init__(position, path, groups, hp)
        self.obstacles = obstacles
        self.vector = pygame.math.Vector2(*vector)
        self.speed = speed
        self.orientation = 'vertical'
        self.rotation = 0

    def _move_action(self): pass

    def _move(self, speed):
        self.rect.x += self.vector.x * speed
        self._collision('horisontal')
        self.rect.y += self.vector.y * speed
        self._collision('vertical')

        self.position = pygame.math.Vector2(self.rect.topleft)
        self._move_action()

    def _collision(self, direction):
        for sprite in self.obstacles:
            if sprite.rect.colliderect(self.rect) and self is not sprite:
                if sprite.__class__.__name__ != 'Shell':
                    if direction == 'horisontal':
                        if self.vector.x > 0:
                            self.rect.right = sprite.rect.left
                        if self.vector.x < 0:
                            self.rect.left = sprite.rect.right
                    elif direction == 'vertical':
                        if self.vector.y > 0:
                            self.rect.bottom = sprite.rect.top
                        if self.vector.y < 0:
                            self.rect.top = sprite.rect.bottom

    def _rotate_action(self, degree):
        self.rotation = degree
        self._set_orientation()
        self._set_vector()
    
    def _set_orientation(self):
        if self.rotation in (0, 180):
            self.orientation = 'vertical'
        elif self.rotation in (-90, 90):
            self.orientation = 'horisontal'

    def _set_vector(self):
        if self.rotation == 0:     self.vector = pygame.math.Vector2(0, -1)
        elif self.rotation == 180: self.vector = pygame.math.Vector2(0, 1)
        elif self.rotation ==  90: self.vector = pygame.math.Vector2(-1, 0)
        elif self.rotation == -90: self.vector = pygame.math.Vector2(1, 0)

    def _additional_update(self):
        self.vector.x = 0
        self.vector.y = 0
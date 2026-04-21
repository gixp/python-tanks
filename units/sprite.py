import pygame


class Sprite(pygame.sprite.Sprite):

    def __init__(self, position, path, groups):
        super().__init__(groups)
        self._set_image(path)
        self.rect = self.image.get_rect(topleft = position)
        self.position = pygame.math.Vector2(position)

    def _remove(self):
        for group in self.groups():
            group.remove(self)

    def _draw(self, surface, position):
        surface.blit(self.image, position)

    def _rotate(self, degree):
        self.image = pygame.transform.rotate(self.image_origin, degree)
        self._rotate_action(degree)

    def _set_image(self, path):
        self.image_origin = pygame.image.load(path).convert_alpha()
        self.image = self.image_origin

    def _input(self): pass

    def _rotate_action(self, degree): pass

    def debug(self): pass

    def _additional_update(self): pass

    def update(self, surface, position):
        self.debug()
        self._input()
        self._draw(surface, position)
        self._additional_update()
import pygame


class Camera(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.half_width = self.surface.get_size()[0] // 2
        self.half_height = self.surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(0,0)

    def custom_draw(self):
        self.offset.x = self.player.rect.centerx - self.half_width
        self.offset.y = self.player.rect.centery - self.half_height

        for sprite in self.sprites():
            position = sprite.rect.topleft - self.offset
            sprite.update(self.surface, position)

    def set_player(self, player):
        self.player = player
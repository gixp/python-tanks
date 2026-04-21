import pygame


class Hood():

    def __init__(self, player):
        self.player = player
        self.width, self.height = pygame.display.get_surface().get_size()
        self.surface = pygame.display.get_surface()

        path_background = 'assets/hood_bg.png'
        self.image_background = pygame.image.load(path_background).convert_alpha()

        path_hp = 'assets/hp.png'
        self.image_hp = pygame.image.load(path_hp).convert_alpha()

        path_ammunition = 'assets/amm.png'
        self.image_ammunition = pygame.image.load(path_ammunition).convert_alpha()

    def _draw(self):
        if self.player.alive:
            self._draw_background()

            self._draw_hp()
            self._draw_ammunition()
            # self.player.hp, self.=w/2-100
            # self.player.ammunition, x=w/2-20
            # self.player.turret.reloading//100, x=w/2+40
            # self.player.rect.center, x=w-200, y=h-50
        else:
            self._draw_info(
                info = 'Died', 
                position = (
                    self.width / 2 - 80, 
                    self.height / 2 - 200
                ),
                font_size = 100,
                background=(0, 0, 0)
            )

    def _draw_background(self):
        self._draw_image(self.image_background, (self.width / 2 - 100, 0))

    def _draw_hp(self):
        self._draw_image(self.image_hp, (self.width / 2 - 85, 15))
        self._draw_info(self.player.hp, (self.width / 2 - 55, 10))

    def _draw_ammunition(self):
        self._draw_image(self.image_ammunition, (self.width / 2 + 20, 3))
        self._draw_info(self.player.ammunition, (self.width / 2 + 40, 10))

    def _draw_info(self, info, position, font_size=50, color=(255, 255, 255), background=None):
        font = pygame.font.Font(None, font_size)
        font_surface = font.render(str(info), True, color)
        font_rect = font_surface.get_rect(topleft=position)
        if background:
            pygame.draw.rect(self.surface, background, font_rect)
        self.surface.blit(font_surface, font_rect)

    def _draw_image(self, image, position):
        self.surface.blit(image, position)
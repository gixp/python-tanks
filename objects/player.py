import pygame
import sprites
import settings


class Player(sprites.Tank):
    
    def __init__(self, position, sprites):
        super().__init__(
            position, 
            paths = {
                "hull": "assets/body_green.png", 
                "turret": "assets/head_green.png", 
                "shell": "assets/bullet.png",
                "destroyed": "assets/body_green_destroyed.png"
            }, 
            groups = [sprites['visible'], sprites['obstacle'], sprites['object']],
            hp = settings.player.hp, 
            speed = settings.player.speed, 
            obstacles = sprites['obstacle'], 
            visibles = sprites['visible'], 
            ammunition = settings.player.ammunition,
            objects = sprites['object'],
            damage = settings.player.damage, 
            shell_speed = settings.player.shell_speed,
            reloading_time = settings.player.reloading_time
        )

    def _input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self._rotate(0)
            self._move(self.speed)
        elif keys[pygame.K_s]:
            self._rotate(180)
            self._move(self.speed)
        elif keys[pygame.K_a]:
            self._rotate(90)
            self._move(self.speed)
        elif keys[pygame.K_d]:
            self._rotate(-90)
            self._move(self.speed)

        if keys[pygame.K_UP]:
            self.turret._rotate(0)
        elif keys[pygame.K_DOWN]:
            self.turret._rotate(180)
        elif keys[pygame.K_LEFT]:
            self.turret._rotate(90)
        elif keys[pygame.K_RIGHT]:
            self.turret._rotate(-90)
        
        if keys[pygame.K_SPACE]:
            self._shot()
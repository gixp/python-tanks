import pygame
import sprites
import random
import settings


class Enemy(sprites.Tank):
    
    def __init__(self, position, sprites, player):
        super().__init__(
            position, 
            paths = {
                "hull": "assets/body_brown.png", 
                "turret": "assets/head_brown.png", 
                "shell": "assets/bullet.png",
                "destroyed": "assets/body_brown_destroyed.png",
            }, 
            groups = [sprites['visible'], sprites['obstacle'], sprites['object']],
            hp = settings.enemy.hp, 
            speed = settings.enemy.speed, 
            obstacles = sprites['obstacle'], 
            visibles = sprites['visible'], 
            ammunition = settings.enemy.ammunition,
            objects = sprites['object'],
            damage = settings.enemy.damage,
            shell_speed = settings.enemy.shell_speed,
            reloading_time = settings.enemy.reloading_time
        )
        self.shot_probability = settings.enemy.shot_probability
        self.player = player

    def _input(self): 
        rotate_coef = settings.enemy.move_rotate_coef
        
        directions = [0, 180, 90, -90]

        for _ in range(rotate_coef - len(directions)):
            directions.append(self.rotation)

        dir_id = random.randint(0, len(directions) - 1)

        self._rotate(directions[dir_id])
        self._move(self.speed)

    def _focus_enemy(self):
        x_distance = abs(self.view_point[0] - self.player.view_point[0])
        y_distance = abs(self.view_point[1] - self.player.view_point[1])

        if x_distance > y_distance:
            if x_distance <= self.view_range:
                if self.view_point[0] < self.player.view_point[0]:
                    if self._random_choice():
                        self.turret._rotate(-90)
                        if self.player.rect.topleft[1] <= self.view_point[1] <= self.player.rect.bottomleft[1]:
                            self._shot()
                else:
                    if self._random_choice():
                        self.turret._rotate(90)
                        if self.player.rect.topright[1] <= self.view_point[1] <= self.player.rect.bottomright[1]:
                            self._shot()
        else:
            if y_distance <= self.view_range:
                if self.view_point[1] < self.player.view_point[1]:
                    if self._random_choice():
                        self.turret._rotate(180)
                        if self.player.rect.topleft[0] <= self.view_point[0] <= self.player.rect.topright[0]:
                            self._shot()
                else:
                    if self._random_choice():
                        self.turret._rotate(0)
                        if self.player.rect.bottomleft[0] <= self.view_point[0] <= self.player.rect.bottomright[0]:
                            self._shot()

    def _random_choice(self):
        if random.choices([True, False], weights=[self.shot_probability, 1-self.shot_probability]):
            return True

    def _additional_update(self):
        self._focus_enemy()
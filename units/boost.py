import pygame
from units.sprite import Sprite


class Boost(Sprite):

    def __init__(self, position, path, groups, objects, attribute, amount):
        super().__init__(position, path, groups)
        self.objects = objects
        self.attribute = attribute
        self.amount = amount

    def _collision(self):
        for object in self.objects:
            if object.rect.colliderect(self.rect) and object.__class__.__name__ == 'Player':
                self._add_boost(object)
                self._remove()
                
    def _add_boost(self, object):
        amount = getattr(object, self.attribute)
        if hasattr(self, self.attribute + '_origin'):
            amount_origin = getattr(object, self.attribute + '_origin')
            if amount + self.amount <= amount_origin:
                setattr(object, self.attribute, amount + self.amount)
        else:
            setattr(object, self.attribute, amount + self.amount)

    def _additional_update(self):
        self._collision()
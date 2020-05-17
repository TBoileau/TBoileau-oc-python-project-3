import pygame
from pygame.sprite import Sprite

from src.domain.maze.entity.item import Item


class ItemSprite(Sprite):
    def __init__(self, item: Item):
        Sprite.__init__(self)
        self.item: Item = item
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(
                "assets/img/%s.png" % self.item.name
            ).convert_alpha(),
            (50, 50)
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            self.item.case.position.x * 69 + 12,
            self.item.case.position.y * 49 + 33
        )

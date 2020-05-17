import pygame
from pygame.sprite import Sprite

from src.domain.maze.entity.item import Item


class BackpackItemSprite(Sprite):
    def __init__(self, item: Item, x: int, y: int):
        Sprite.__init__(self)
        self.item: Item = item
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(
                "assets/img/%s.png" % self.item.name
            ).convert_alpha(),
            (25, 25)
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

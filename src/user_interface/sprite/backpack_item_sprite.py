"""Import libraries."""
import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface

from config import CurrentPath
from src.domain.maze.entity.item import Item


class BackpackItemSprite(Sprite):
    """
    BackpackItemSprite.

    It contains an instance of Item from domain
    that will be placed in group of sprites
    belonging to ProgressComponent.
    """

    def __init__(self, item: Item, x: int, y: int):
        """
        Define item stripe.

        Add item in backpack.
        Load image from assets folder,
        and place it in progress on a specific place.


        :param item:
        :param x:
        :param y:
        """
        Sprite.__init__(self)
        self.item: Item = item
        self.image: Surface = pygame.transform.scale(
            pygame.image.load(
                CurrentPath + "/assets/img/%s.png" % self.item.name
            ).convert_alpha(),
            (25, 25)
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

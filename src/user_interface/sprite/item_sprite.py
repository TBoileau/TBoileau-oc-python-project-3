"""Import libraries."""
import pygame
from pygame.sprite import Sprite

from config import CurrentPath
from src.domain.maze.entity.item import Item


class ItemSprite(Sprite):
    """
    ItemSprite.

    It contains an instance of Item from domain
    that will be placed in group of sprites
    belonging to CellComponent.
    """

    def __init__(self, item: Item):
        """
        Define item stripe.

        Add item in cell.
        Load image from assets folder,
        and place it in progress on a specific cell.

        :param item:
        """
        Sprite.__init__(self)
        self.item: Item = item
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(
                CurrentPath + "/assets/img/%s.png" % self.item.name
            ).convert_alpha(),
            (50, 50)
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            self.item.case.position.x * 69 + 12,
            self.item.case.position.y * 49 + 33
        )

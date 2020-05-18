"""Import libraries."""
import pygame
from pygame.sprite import Sprite

from config import CurrentPath
from src.domain.maze.entity.enemy import Enemy


class EnemySprite(Sprite):
    """
    EnemySprite.

    It contains an instance of Enemy from domain
    that will be placed in group of sprites
    belonging to MazeComponent.
    """

    def __init__(self, enemy: Enemy):
        """
        Define enemy stripe.

        Add enemy in mazess UI.
        Load image from assets folder,
        and place it in mazess on the end cell.

        :param enemy:
        """
        Sprite.__init__(self)
        self.enemy: Enemy = enemy
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(
                CurrentPath + "/assets/img/enemy.png"
            ).convert_alpha(),
            (50, 50)
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            self.enemy.case.position.x * 69 + 12,
            self.enemy.case.position.y * 49 + 33
        )

import pygame
from pygame.sprite import Sprite

from src.domain.maze.entity.enemy import Enemy


class EnemySprite(Sprite):
    def __init__(self, enemy: Enemy):
        Sprite.__init__(self)
        self.enemy: Enemy = enemy
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load("assets/img/enemy.png").convert_alpha(),
            (50, 50)
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            self.enemy.case.position.x * 69 + 12,
            self.enemy.case.position.y * 49 + 33
        )

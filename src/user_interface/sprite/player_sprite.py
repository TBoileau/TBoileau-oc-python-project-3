from typing import Dict

import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface

from config import CurrentPath
from src.domain.maze.entity.player import Player
from src.domain.maze.exception.bad_cell_exception import BadCellException
from src.domain.maze.value_object.direction import Direction


class PlayerSprite(Sprite):
    def __init__(self, player: Player):
        Sprite.__init__(self)
        self.player = player
        self.images: Dict[str, Surface] = {
            Direction.UP: pygame.transform.scale(
                pygame.image.load(
                    CurrentPath + "/assets/img/north.png"
                ).convert_alpha(),
                (50, 50)
            ),
            Direction.DOWN: pygame.transform.scale(
                pygame.image.load(
                    CurrentPath + "/assets/img/south.png"
                ).convert_alpha(),
                (50, 50)
            ),
            Direction.RIGHT: pygame.transform.scale(
                pygame.image.load(
                    CurrentPath + "/assets/img/east.png"
                ).convert_alpha(),
                (50, 50)
            ),
            Direction.LEFT: pygame.transform.scale(
                pygame.image.load(
                    CurrentPath + "/assets/img/west.png"
                ).convert_alpha(),
                (50, 50)
            )
        }
        self.image = self.images[Direction.RIGHT]
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            self.player.case.position.x * 69 + 12,
            self.player.case.position.y * 49 + 33
        )

    def move(self, direction):
        try:
            self.player.move(direction)
        except BadCellException:
            print("Bad direction")
        self.rect.topleft = (
            self.player.case.position.x * 69 + 12,
            self.player.case.position.y * 49 + 33
        )
        self.image = self.images[direction]

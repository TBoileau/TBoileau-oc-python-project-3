"""Import libraries."""
import pygame
from pygame.sprite import Group

from config import CurrentPath
from src.domain.maze.entity.case import Case
from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.wall import Wall
from src.user_interface.sprite.item_sprite import ItemSprite


class CellComponent:
    """
    CellComponent.

    This component display a cell with a group of sprite
    who contains an item to pick up.
    """

    def __init__(self, cell: Cell, window: pygame.Surface):
        """
        Create and position a cell in mazess.

        :param cell:
        :param window:
        """
        self.cell: Cell = cell
        self.window: pygame.Surface = window
        self.x: int = cell.position.x * 69
        self.y: int = cell.position.y * 49 + 50
        self.group: Group = pygame.sprite.Group()
        if isinstance(cell, Wall):
            self.y -= 17
        if isinstance(self.cell, Case) and self.cell.item is not None:
            self.item: ItemSprite = ItemSprite(self.cell.item)
            self.group.add(self.item)

    def render(self):
        """
        Display a case cell.

        Add a wall on top of it, if the instance of item
        from the domain is a Wall.
        """
        self.window.blit(
            pygame.transform.scale(
                pygame.image.load(
                    CurrentPath + '/assets/img/case.png'
                ).convert(),
                (69, 98)
            ),
            (self.x, self.y),
            (0, 0, 69, 66)
        )

        if isinstance(self.cell, Wall):
            self.window.blit(
                pygame.transform.scale(
                    pygame.image.load(
                        CurrentPath + '/assets/img/wall.png'
                    ).convert(),
                    (69, 66)
                ),
                (self.x, self.y),
                (0, 0, 69, 66)
            )

        self.group.draw(self.window)

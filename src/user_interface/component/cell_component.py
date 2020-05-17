import pygame

from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.wall import Wall


class CellComponent:
    def __init__(self, cell: Cell, window: pygame.Surface):
        self.cell: Cell = cell
        self.window: pygame.Surface = window
        self.x: int = cell.position.x * 69
        self.y: int = cell.position.y * 49 + 17
        if isinstance(cell, Wall):
            self.y -= 17

    def render(self):
        self.window.blit(
            pygame.transform.scale(
                pygame.image.load('assets/img/case.png').convert(),
                (69, 98)
            ),
            (self.cell.position.x * 69, self.cell.position.y * 49 + 17),
            (0, 0, 69, 66)
        )
        if isinstance(self.cell, Wall):
            self.window.blit(
                pygame.transform.scale(
                    pygame.image.load('assets/img/wall.png').convert(),
                    (69, 66)
                ),
                (self.cell.position.x * 69, self.cell.position.y * 49),
                (0, 0, 69, 66)
            )

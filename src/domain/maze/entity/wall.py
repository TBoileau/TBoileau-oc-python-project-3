"""Import libraries."""
from src.domain.maze.entity.cell import Cell


class Wall(Cell):
    """
    Wall.

    Child class of Cell.
    A wall can not be reach by a player.
    """

    pass

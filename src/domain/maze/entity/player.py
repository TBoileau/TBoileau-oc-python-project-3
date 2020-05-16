from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.character import Character
from src.domain.maze.exception.bad_cell_exception import BadCellException
from src.domain.maze.value_object.direction import Direction


class Player(Character):
    def __init__(self, name: str, maze):
        self.cell: Cell
        self.maze = maze
        self.name: str = name

    def start(self):
        self.cell = self.maze.start

    def move(self, direction: str):
        assert direction in Direction.ALL
        next_cell: Cell = self.maze.next_cell(self.cell, direction)
        if next_cell is None:
            raise BadCellException
        self.cell = next_cell

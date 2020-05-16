from typing import List, Union

from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.end import End
from src.domain.maze.entity.maze import Maze
from src.domain.maze.value_object.direction import Direction


class MazeResolver:
    def __init__(self, maze: Maze):
        self.maze: Maze = maze
        self.directions: List = []
        self.cells: List[Union[Cell, None]] = [None]

    def resolve(self) -> "MazeResolver":
        self.scan(self.maze.start, Direction.RIGHT)
        return self

    def scan(self, cell: Cell, direction: str) -> bool:
        self.cells.append(cell)
        self.directions.append(direction)
        next_cell: Union[None, Cell] = self.maze.next_cell(cell, direction)

        if next_cell in self.cells:
            return False

        if isinstance(next_cell, End):
            print("ici")
            return True

        for new_direction in Direction.ALL:
            path_founded = self.scan(next_cell, new_direction)
            if Direction.REVERSE[direction] == new_direction \
                    or not path_founded:
                self.directions.pop()
                continue
            if path_founded:
                return True

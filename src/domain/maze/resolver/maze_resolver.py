from typing import List, Union

from src.domain.maze.entity.case import Case
from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.maze import Maze
from src.domain.maze.value_object.direction import Direction


class MazeResolver:
    def __init__(self, maze: Maze):
        self.maze: Maze = maze
        self.directions: List[str] = []
        self.cells: List[Union[Cell, None]] = [None]

    def resolve(self, goal: Case, return_to_start: bool) -> "MazeResolver":
        self.directions = []
        self.cells = [None]
        self.scan(self.maze.start, Direction.RIGHT, goal)
        if return_to_start:
            direction_to_start: List[str] = self.directions.copy()
            direction_to_start.reverse()
            for direction in direction_to_start:
                self.directions.append(Direction.REVERSE[direction])

        return self

    def scan(self, case: Case, direction: str, goal: Case) -> bool:
        self.cells.append(case)
        self.directions.append(direction)
        next_case: Union[None, Case] = self.maze.next_case(case, direction)

        if next_case in self.cells:
            return False

        if next_case == goal:
            return True

        for new_direction in Direction.ALL:
            path_founded = self.scan(next_case, new_direction, goal)
            if Direction.REVERSE[direction] == new_direction \
                    or not path_founded:
                self.directions.pop()
                continue
            if path_founded:
                return True

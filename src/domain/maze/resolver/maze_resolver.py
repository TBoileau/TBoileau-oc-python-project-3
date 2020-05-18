"""Import libraries."""
from typing import List, Union

from src.domain.maze.entity.case import Case
from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.maze import Maze
from src.domain.maze.store.direction import Direction


class MazeResolver:
    """
    MazeResolver.

    This service resolve the mazess by exploring all the possibilities.
    """

    def __init__(self, maze: Maze):
        """
        Initialize the mazess resolver.

        :param maze:
        """
        self.maze: Maze = maze
        self.directions: List[str] = []
        self.cells: List[Union[Cell, None]] = [None]

    def resolve(self, goal: Case, return_to_start: bool) -> "MazeResolver":
        """
        Resolve the mazess.

        Determine all directions from the start to the goal cell.
        If we need to return to the start cell, we reverse directions and
        add to this last one.

        :param goal:
        :param return_to_start:
        :return:
        """
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
        """
        Scan a cell with a specific direction.

        Append the cell in array, and add the current direction.
        If the cell is a wall,we stop the method by returing false.
        Otherwise we check if the goal is achieved
        and stop the method by returning true.
        Finally, we're scanning all directions from the current cell.

        :param case:
        :param direction:
        :param goal:
        :return:
        """
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

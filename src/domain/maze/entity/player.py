from typing import List

from src.domain.maze.entity.case import Case
from src.domain.maze.entity.character import Character
from src.domain.maze.entity.item import Item
from src.domain.maze.exception.bad_cell_exception import BadCellException
from src.domain.maze.store.direction import Direction


class Player(Character):
    def __init__(self, name: str, maze):
        super().__init__(name, maze)
        self.items: List[Item] = []
        self.finished: bool = False
        self.win: bool = False

    def start(self):
        self.case = self.maze.start

    def move(self, direction: str):
        assert direction in Direction.ALL
        next_case: Case = self.maze.next_case(self.case, direction)
        if next_case is None:
            raise BadCellException
        self.case = next_case
        if self.case.item is not None:
            self.items.append(self.case.item)
            self.case.item.pick_up()
        if self.case == self.maze.end:
            self.finished = True
            self.win = len(self.items) == len(self.maze.items)

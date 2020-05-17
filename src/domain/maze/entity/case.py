from typing import Union

from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.item import Item
from src.domain.maze.value_object.position import Position


class Case(Cell):
    def __init__(self, position: Position):
        super().__init__(position)
        self.item: Union[None, Item] = None

    def add_item(self, item: str):
        self.item = Item(item, self)

    def remove_item(self):
        self.item = None

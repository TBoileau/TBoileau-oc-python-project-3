"""Import libraries."""
from typing import Union

from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.item import Item
from src.domain.maze.value_object.position import Position


class Case(Cell):
    """
    Case.

    Child of Cell, a case is a empty cell that can be use by player.
    A case can also have a item in it.
    """

    def __init__(self, position: Position):
        """
        Initialize item at none.

        :param position:
        """
        super().__init__(position)
        self.item: Union[None, Item] = None

    def add_item(self, item: str):
        """
        Add an item.

        :param item:
        """
        self.item = Item(item, self)

    def remove_item(self):
        """Remove the item."""
        self.item = None

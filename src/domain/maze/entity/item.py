"""Import libraries."""
from typing import Union, Any


class Item:
    """
    Item.

    An item on a cell can be pick up by the player.
    So, it will be remove from the cell
    and place in player backpack.
    """

    def __init__(self, name: str, case):
        """
        Define name and case.

        :param name:
        :param case:
        """
        self.name: str = name
        self.case: Union[Any, None] = case

    def pick_up(self):
        """Pick up the item and remove it from the cell."""
        self.case.remove_item()

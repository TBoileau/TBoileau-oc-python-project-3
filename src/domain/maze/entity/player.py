"""Import libraries."""
from typing import List

from src.domain.maze.entity.case import Case
from src.domain.maze.entity.character import Character
from src.domain.maze.entity.item import Item
from src.domain.maze.exception.bad_cell_exception import BadCellException
from src.domain.maze.store.direction import Direction


class Player(Character):
    """
    Player.

    Child class of Character.
    A player has a list of items in his backpack.
    And a player is always on a cell.
    Then, a player can move on the mazess.
    """

    def __init__(self, name: str, maze):
        """
        Initialize player.

        :param name:
        :param maze:
        """
        super().__init__(name, maze)
        self.items: List[Item] = []
        self.finished: bool = False

    @property
    def win(self):
        """
        Check if player as picked up all items.

        :return:
        """
        return len(self.items) == len(self.maze.items)

    def start(self):
        """Place the player of the start case of mazess."""
        self.case = self.maze.start

    def move(self, direction: str):
        """
        Move the player on mazess.

        A player can move on the mazess if the next case is empty.
        If the next case contains a item, than the player pick up
        and place it in his backpack.
        Finally, if the player reaches the end,
        we check if he has in his backpack all the items
        that were present in the mazess, then the player can win the game.

        :param direction:
        """
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

"""Import libraries."""
from typing import Tuple, Dict

from src.domain.maze.store.direction import Direction


class Position:
    """
    Position.

    This class is a value object of a position, define by a X and Y points.
    """

    def __init__(self, x: int, y: int):
        """
        Define X and Y points.

        :param x:
        :param y:
        """
        self.x: int = x
        self.y: int = y

    def next_position(self, direction: str) -> "Position":
        """
        Return new position.

        According to a direction and the current position.

        :param direction:
        :return:
        """
        directions: Tuple[Dict[str, int], Dict[str, int]] = (
            {
                Direction.UP: 0,
                Direction.DOWN: 0,
                Direction.RIGHT: 1,
                Direction.LEFT: -1
            },
            {
                Direction.UP: -1,
                Direction.DOWN: 1,
                Direction.RIGHT: 0,
                Direction.LEFT: 0
            }
        )
        return Position(
            self.x + directions[0][direction],
            self.y + directions[1][direction]
        )

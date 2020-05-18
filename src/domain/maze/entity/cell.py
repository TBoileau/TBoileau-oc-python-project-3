"""Import libraries."""
from src.domain.maze.value_object.position import Position


class Cell:
    """
    Cell.

    Abstract class.
    """

    def __init__(self, position: Position):
        """
        Define the position of the cell.

        :param position:
        """
        self.position: Position = position

"""Import libraries."""
from abc import abstractmethod, ABC
from typing import List


class MazeGeneratorPort(ABC):
    """
    MazeGeneratorPort.

    This interface is a port
    """

    START: int = 2
    WALL: int = 0
    END: int = 3
    EMPTY: int = 1

    @abstractmethod
    def generate(self, x: int, y: int) -> List[List[int]]:
        """
        Generate a mazess.

        Generate a mazess that contains 4 types of cell.
        0 : wall
        1 : empty cell
        2 : start cell
        3 : end cell.

        :param x:
        :param y:
        :return:
        """
        pass

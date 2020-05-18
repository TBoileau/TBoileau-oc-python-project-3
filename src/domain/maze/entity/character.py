"""Import libraries."""
from src.domain.maze.entity.case import Case


class Character:
    """
    Character.

    Abstract class.
    """

    def __init__(self, name: str, maze):
        """
        Define case, mazess and name of character.

        :param name:
        :param maze:
        """
        self.case: Case
        self.maze = maze
        self.name: str = name

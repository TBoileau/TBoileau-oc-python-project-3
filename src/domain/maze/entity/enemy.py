"""Import libraries."""
from src.domain.maze.entity.character import Character


class Enemy(Character):
    """
    Enemy.

    Child class of Character.
    """

    def start(self):
        """Place the enemy of the end case of maze."""
        self.case = self.maze.end

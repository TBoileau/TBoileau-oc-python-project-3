from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.character import Character


class Player(Character):
    def __init__(self, name: str, maze):
        self.cell: Cell
        self.maze = maze
        self.name: str = name

    def start(self):
        self.cell = self.maze.start

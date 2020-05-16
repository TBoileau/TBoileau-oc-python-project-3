from src.domain.maze.entity.cell import Cell


class Character:
    def __init__(self, name: str, maze):
        self.cell: Cell
        self.maze = maze
        self.name: str = name

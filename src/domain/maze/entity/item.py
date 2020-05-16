from src.domain.maze.entity.cell import Cell


class Item:
    def __init__(self, name: str, cell: Cell):
        self.name: str = name
        self.cell: Cell = cell

from src.domain.maze.value_object.position import Position


class Cell:
    def __init__(self, position: Position):
        self.position: Position = position

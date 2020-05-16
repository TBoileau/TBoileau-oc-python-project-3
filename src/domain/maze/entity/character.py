from src.domain.maze.entity.case import Case


class Character:
    def __init__(self, name: str, maze):
        self.case: Case
        self.maze = maze
        self.name: str = name

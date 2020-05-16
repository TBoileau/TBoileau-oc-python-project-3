from typing import Tuple, Dict

from src.domain.maze.value_object.direction import Direction


class Position:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

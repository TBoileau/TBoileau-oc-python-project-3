from typing import List, Dict


class Direction:
    UP: str = "up"
    DOWN: str = "down"
    LEFT: str = "left"
    RIGHT: str = "right"
    ALL: List[str] = [UP, DOWN, LEFT, RIGHT]
    REVERSE: Dict[str, str] = {
        UP: DOWN,
        DOWN: UP,
        RIGHT: LEFT,
        LEFT: RIGHT
    }

import random
from typing import List, Tuple, Dict

from src.domain.maze.store.direction import Direction


class MazeGenerator:
    START: int = 2
    WALL: int = 0
    END: int = 3
    EMPTY: int = 1

    @staticmethod
    def new_position(
            position:
            Tuple[int, int],
            pad: int, direction: str
    ) -> Tuple[int, int]:
        directions: Tuple[Dict[str, int], Dict[str, int]] = (
            {
                Direction.UP: 0,
                Direction.DOWN: 0,
                Direction.RIGHT: pad,
                Direction.LEFT: -pad
            },
            {
                Direction.UP: -pad,
                Direction.DOWN: pad,
                Direction.RIGHT: 0,
                Direction.LEFT: 0
            }
        )
        return (
            position[0] + directions[0][direction],
            position[1] + directions[1][direction]
        )

    @staticmethod
    def generate(x: int, y: int) -> List[List[int]]:
        cells: List[List[int]] = [
            [0 for x in range(2 * x + 1)] for y in range(2 * y + 1)
        ]

        temp_cells: List[Tuple[int, int]] = []

        (rx, ry) = (
            (2 * random.randrange(x) + 1),
            (2 * random.randrange(y) + 1)
        )

        cells[ry][rx] = MazeGenerator.EMPTY

        for direction in Direction.ALL:
            nx, ny = MazeGenerator.new_position((rx, ry), 2, direction)
            if 0 <= nx < 2 * x + 1 and 0 <= ny < 2 * y + 1:
                cells[ny][nx] = MazeGenerator.START
                temp_cells.append((nx, ny))

        while temp_cells:
            rx, ry = random.choice(temp_cells)
            temp_cells.remove((rx, ry))
            cells[ry][rx] = MazeGenerator.EMPTY
            neighbours: List[Tuple[int, int]] = []
            for direction in Direction.ALL:
                nx, ny = MazeGenerator.new_position((rx, ry), 2, direction)
                if 0 <= nx < 2 * x + 1 \
                        and 0 <= ny < 2 * x + 1 \
                        and cells[ny][nx] == MazeGenerator.EMPTY:
                    neighbours.append((nx, ny))

            for direction in Direction.ALL:
                nx, ny = MazeGenerator.new_position((rx, ry), 2, direction)
                if 0 <= nx < 2 * x + 1 \
                        and 0 <= ny < 2 * x + 1 \
                        and cells[ny][nx] == MazeGenerator.WALL:
                    cells[ny][nx] = MazeGenerator.START
                    temp_cells.append((nx, ny))

            if len(neighbours) > 0:
                nx, ny = random.choice(neighbours)
                cells[int((nx + rx) / 2)][int((ny + ry) / 2)] = 1
                cells[ny][nx] = MazeGenerator.EMPTY

        sx, sy = (0, 2 * random.randrange(y) + 1)
        ex, ey = ((2 * x), 2 * random.randrange(y) + 1)
        cells[sy][sx] = MazeGenerator.START
        cells[ey][ex] = MazeGenerator.END

        return cells

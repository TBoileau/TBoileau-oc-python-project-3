"""Import libraries."""
from typing import List

from src.domain.maze.port.maze_generator_port import MazeGeneratorPort


class MazeGenerator(MazeGeneratorPort):
    """
    MazeGenerator.

    This class generate a mazess with file in assets folder
    by implementing the MazeGeneratorPort interface.
    """

    def generate(self, x: int, y: int) -> List[List[int]]:
        """
        Generate a mazess.

        With assets/mazess/maze, return a maze
        that contains 4 types of cell :
        0 : wall
        1 : empty cell
        2 : start cell
        3 : end cell.

        :param x:
        :param y:
        :return:
        """
        with open("assets/maze", "r") as lines:
            x, y = 0, 0
            cells: List[List[int]] = []
            for line in lines:
                cells.append([])
                for cell in line:
                    if cell != "\n":
                        cells[y].append(int(cell))
                        x += 1
                x = 0
                y += 1
            print(cells)
            return cells

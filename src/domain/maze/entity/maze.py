"""Import libraries."""
import random
from typing import List, Union

from src.domain.maze.entity.case import Case
from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.end import End
from src.domain.maze.entity.enemy import Enemy
from src.domain.maze.entity.player import Player
from src.domain.maze.entity.start import Start
from src.domain.maze.entity.wall import Wall
from src.domain.maze.port.maze_generator_port import MazeGeneratorPort
from src.domain.maze.value_object.position import Position


class Maze:
    """
    Maze.

    A mazess contains a set of cells,
    a player and his enemy, as well as a set of items.
    """

    def __init__(
            self,
            maze_generator: MazeGeneratorPort,
            x: int,
            y: int,
            player_name: str,
            enemy_name: str,
            items: List[str]
    ):
        """
        Initialize mazess.

        Check if the player and enemy names are not empty.
        Check if the number of case in x and y are greater than 2.
        We use the mazess generator to generate the cells of mazess.

        :param x:
        :param y:
        :param player_name:
        :param enemy_name:
        :param items:
        """
        player_name = player_name.strip()
        enemy_name = enemy_name.strip()
        assert x > 2
        assert y > 2
        assert len(items) > 0
        assert player_name != ""
        assert enemy_name != ""
        self.maze_generator: MazeGeneratorPort = maze_generator
        self.x: int = x
        self.y: int = y
        self.items: List[str] = items
        self.player: Player = Player(player_name, self)
        self.enemy: Enemy = Enemy(enemy_name, self)
        self.cells: List[Cell] = []
        self.start: Start
        self.end: End
        self.generate()

    def generate(self):
        """
        Generate mazess.

        Using the MazeGenerator for populate cells.
        """
        rows = self.maze_generator.generate(self.x, self.y)
        empty_cases: List[Case] = []
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                if rows[y][x] == MazeGeneratorPort.EMPTY:
                    case: Case = Case(Position(x, y))
                    self.cells.append(case)
                    empty_cases.append(case)
                if rows[y][x] == MazeGeneratorPort.WALL:
                    self.cells.append(Wall(Position(x, y)))
                if rows[y][x] == MazeGeneratorPort.START:
                    self.start = Start(Position(x, y))
                    self.cells.append(self.start)
                    self.player.start()
                if rows[y][x] == MazeGeneratorPort.END:
                    self.end = End(Position(x, y))
                    self.cells.append(self.end)
                    self.enemy.start()

        for item in self.items:
            random_cell: Case = random.choice(empty_cases)
            random_cell.add_item(item)
            empty_cases.remove(random_cell)

    def get_case(self, position: Position) -> Union[Cell, None]:
        """
        Get a case from his position.

        :param position:
        :return:
        """
        for cell in self.cells:
            if cell.position.x == position.x \
                    and cell.position.y == position.y \
                    and isinstance(cell, Case):
                return cell
        return None

    def next_case(self, case: Case, direction: str) -> Union[Case, None]:
        """
        Get the next case.

        According to a direction and the current case.

        :param case:
        :param direction:
        :return:
        """
        next_position: Position = case.position.next_position(direction)
        return self.get_case(next_position)

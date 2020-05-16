from typing import List, Union

from src.domain.maze.entity.cell import Cell
from src.domain.maze.entity.empty import Empty
from src.domain.maze.entity.end import End
from src.domain.maze.entity.enemy import Enemy
from src.domain.maze.entity.player import Player
from src.domain.maze.entity.start import Start
from src.domain.maze.entity.wall import Wall
from src.domain.maze.generator.maze_generator import MazeGenerator
from src.domain.maze.value_object.position import Position


class Maze:
    def __init__(self, x: int, y: int, player_name: str, enemy_name: str):
        player_name = player_name.strip()
        enemy_name = enemy_name.strip()
        assert x > 2
        assert y > 2
        assert player_name != ""
        assert enemy_name != ""
        self.x: int = x
        self.y: int = y
        self.player: Player = Player(player_name, self)
        self.enemy: Enemy = Enemy(enemy_name, self)
        self.cells: List[Cell] = []
        self.start: Start
        self.end: End
        self.generate()

    def generate(self):
        rows = MazeGenerator.generate(self.x, self.y)
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                if rows[y][x] == MazeGenerator.EMPTY:
                    self.cells.append(Empty(Position(x, y)))
                if rows[y][x] == MazeGenerator.WALL:
                    self.cells.append(Wall(Position(x, y)))
                if rows[y][x] == MazeGenerator.START:
                    self.start = Start(Position(x, y))
                    self.cells.append(self.start)
                    self.player.start()
                if rows[y][x] == MazeGenerator.END:
                    self.end = End(Position(x, y))
                    self.cells.append(self.end)
                    self.enemy.start()

    def get_cell(self, position: Position) -> Union[Cell, None]:
        for cell in self.cells:
            if cell.position.x == position.x \
                    and cell.position.y == position.y \
                    and (isinstance(cell, Empty) or isinstance(cell, End)):
                return cell
        return None

    def next_cell(self, cell: Cell, direction: str) -> Union[Cell, None]:
        next_position: Position = cell.position.next_position(direction)
        return self.get_cell(next_position)

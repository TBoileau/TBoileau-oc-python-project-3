import pytest

from src.domain.maze.entity.maze import Maze
from src.domain.maze.exception.bad_cell_exception import BadCellException
from src.domain.maze.value_object.direction import Direction


def test_if_player_move_on_maze_to_the_end():
    maze: Maze = Maze(3, 3, "Player")
    maze.player.move(Direction.RIGHT)
    assert maze.start != maze.player.cell


def test_if_failed_with_wrong_direction():
    with pytest.raises(AssertionError):
        maze: Maze = Maze(5, 5, "Player")
        maze.player.move("fail")


def test_if_failed_with_bad_direction():
    with pytest.raises(BadCellException):
        maze: Maze = Maze(5, 5, "Player")
        maze.player.move(Direction.DOWN)

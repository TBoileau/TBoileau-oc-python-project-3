from typing import List

import pytest

from src.domain.maze.entity.case import Case
from src.domain.maze.entity.maze import Maze
from src.domain.maze.exception.bad_cell_exception import BadCellException
from src.domain.maze.resolver.maze_resolver import MazeResolver
from src.domain.maze.value_object.direction import Direction


def test_if_player_move_on_maze_to_the_end():
    maze: Maze = Maze(3, 3, "Mac Gyver", "Guard", ['ether', 'needle', 'wood'])
    steps: List[Case, bool] = [
        (maze.cases_with_items[0], True),
        (maze.cases_with_items[1], True),
        (maze.cases_with_items[2], True),
        (maze.end, False)
    ]
    for step in steps:
        maze_resolver: MazeResolver = MazeResolver(maze).resolve(*step)
        for direction in maze_resolver.directions:
            maze.player.move(direction)
    assert maze.end == maze.player.case
    assert len(maze.player.items) == 3


def test_if_failed_with_wrong_direction():
    with pytest.raises(AssertionError):
        maze: Maze = Maze(
            5,
            5,
            "Mac Gyver",
            "Guard",
            ['ether', 'needle', 'wood']
        )
        maze.player.move("fail")


def test_if_failed_with_bad_direction():
    with pytest.raises(BadCellException):
        maze: Maze = Maze(
            5,
            5,
            "Mac Gyver",
            "Guard",
            ['ether', 'needle', 'wood']
        )
        maze.player.move(Direction.DOWN)

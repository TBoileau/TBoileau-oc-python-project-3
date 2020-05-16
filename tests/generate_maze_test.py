import pytest

from src.domain.maze.entity.enemy import Enemy
from src.domain.maze.entity.maze import Maze
from src.domain.maze.entity.player import Player


def test_if_maze_creation_is_successful():
    maze: Maze = Maze(5, 5, "Player")
    assert maze.x == 5
    assert maze.y == 5
    assert isinstance(maze.player, Player)
    assert maze.player.name == "Player"
    assert isinstance(maze.enemy, Enemy)
    assert len(maze.cells) == 121


def test_if_x_and_x_are_too_small():
    with pytest.raises(AssertionError):
        Maze(2, 2, "Player")


def test_if_player_is_empty():
    with pytest.raises(AssertionError):
        Maze(5, 5, "")


def test_if_player_has_only_space():
    with pytest.raises(AssertionError):
        Maze(5, 5, " ")

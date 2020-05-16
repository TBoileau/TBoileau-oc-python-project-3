import pytest

from src.domain.maze.entity.enemy import Enemy
from src.domain.maze.entity.maze import Maze
from src.domain.maze.entity.player import Player


def test_if_maze_creation_is_successful():
    maze: Maze = Maze(5, 5, "Player", "Guard")
    assert maze.x == 5
    assert maze.y == 5
    assert isinstance(maze.player, Player)
    assert maze.player.name == "Player"
    assert maze.player.cell == maze.start
    assert isinstance(maze.enemy, Enemy)
    assert maze.enemy.name == "Guard"
    assert maze.enemy.cell == maze.end
    assert len(maze.cells) == 121


def test_if_x_and_x_are_too_small():
    with pytest.raises(AssertionError):
        Maze(2, 2, "Player", "Guard")


def test_if_enemy_is_empty():
    with pytest.raises(AssertionError):
        Maze(5, 5, "Player", "")


def test_if_enemy_has_only_space():
    with pytest.raises(AssertionError):
        Maze(5, 5, "Player", " ")


def test_if_player_is_empty():
    with pytest.raises(AssertionError):
        Maze(5, 5, "", "Guard")


def test_if_player_has_only_space():
    with pytest.raises(AssertionError):
        Maze(5, 5, " ", "Guard")

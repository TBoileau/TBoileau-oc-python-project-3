import pytest

from src.domain.maze.entity.enemy import Enemy
from src.domain.maze.entity.maze import Maze
from src.domain.maze.entity.player import Player


def test_if_maze_creation_is_successful():
    maze: Maze = Maze(5, 5, "Mac Gyver", "Guard", ['ether', 'needle', 'wood'])
    assert len(maze.items) == 3
    assert maze.x == 5
    assert maze.y == 5
    assert isinstance(maze.player, Player)
    assert maze.player.name == "Mac Gyver"
    assert maze.player.case == maze.start
    assert isinstance(maze.enemy, Enemy)
    assert maze.enemy.name == "Guard"
    assert maze.enemy.case == maze.end
    assert len(maze.cells) == 121


def test_if_x_and_x_are_too_small():
    with pytest.raises(AssertionError):
        Maze(2, 2, "Mac Gyver", "Guard", ['ether', 'needle', 'wood'])


def test_if_number_of_items_is_not_equal_to_3():
    with pytest.raises(AssertionError):
        Maze(5, 5, "Mac Gyver", "Guard", [])


def test_if_enemy_is_case():
    with pytest.raises(AssertionError):
        Maze(5, 5, "Mac Gyver", "", ['ether', 'needle', 'wood'])


def test_if_enemy_has_only_space():
    with pytest.raises(AssertionError):
        Maze(5, 5, "Mac Gyver", " ", ['ether', 'needle', 'wood'])


def test_if_player_is_case():
    with pytest.raises(AssertionError):
        Maze(5, 5, "", "Guard", ['ether', 'needle', 'wood'])


def test_if_player_has_only_space():
    with pytest.raises(AssertionError):
        Maze(5, 5, " ", "Guard", ['ether', 'needle', 'wood'])

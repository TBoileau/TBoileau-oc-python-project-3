import pytest

from src.domain.maze.entity.case import Case
from src.domain.maze.entity.maze import Maze
from src.domain.maze.exception.bad_cell_exception import BadCellException
from src.domain.maze.resolver.maze_resolver import MazeResolver
from src.domain.maze.store.direction import Direction
from src.infrastructure.adapter.primary.maze_generator import MazeGenerator


def test_if_player_win():
    maze_generator: MazeGenerator = MazeGenerator()
    maze: Maze = Maze(
        maze_generator,
        3,
        3,
        "Mac Gyver",
        "Guard",
        ['ether', 'needle', 'plastic_tube']
    )
    maze_resolver: MazeResolver = MazeResolver(maze)

    def resolve(case: Case, back: bool):
        maze_resolver.resolve(case, back)
        for direction in maze_resolver.directions:
            maze.player.move(direction)

    for cell in maze.cells:
        if isinstance(cell, Case) and cell.item is not None:
            resolve(cell, True)
    resolve(maze.end, False)

    assert maze.end == maze.player.case
    assert len(maze.player.items) == 3
    assert maze.player.finished
    assert maze.player.win


def test_if_player_lose():
    maze_generator: MazeGenerator = MazeGenerator()
    maze: Maze = Maze(
        maze_generator,
        5,
        5,
        "Mac Gyver",
        "Guard",
        ['ether', 'needle', 'plastic_tube']
    )

    maze_resolver: MazeResolver = MazeResolver(maze).resolve(maze.end, False)
    for direction in maze_resolver.directions:
        maze.player.move(direction)

    maze.player.items = []

    assert maze.end == maze.player.case
    assert maze.player.finished
    assert not maze.player.win


def test_if_failed_with_wrong_direction():
    with pytest.raises(AssertionError):
        maze_generator: MazeGenerator = MazeGenerator()
        maze: Maze = Maze(
            maze_generator,
            5,
            5,
            "Mac Gyver",
            "Guard",
            ['ether', 'needle', 'plastic_tube']
        )
        maze.player.move("fail")


def test_if_failed_with_bad_direction():
    with pytest.raises(BadCellException):
        maze_generator: MazeGenerator = MazeGenerator()
        maze: Maze = Maze(
            maze_generator,
            5,
            5,
            "Mac Gyver",
            "Guard",
            ['ether', 'needle', 'plastic_tube']
        )
        maze.player.move(Direction.DOWN)

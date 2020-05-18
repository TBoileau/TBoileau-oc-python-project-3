"""Import libraries."""
from src.domain.maze.entity.maze import Maze
from src.infrastructure.adapter.primary.maze_generator import MazeGenerator
from src.user_interface.component.maze_component import MazeComponent


def run():
    """Instantiate mazess and render the mazess component."""
    maze_generator = MazeGenerator()
    maze: Maze = Maze(
        maze_generator,
        7,
        7,
        "Mac Gyver",
        "Guard",
        ['ether', 'needle', 'plastic_tube']
    )
    component: MazeComponent = MazeComponent(maze)
    component.render()


if __name__ == '__main__':
    run()

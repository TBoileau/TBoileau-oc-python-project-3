"""Import libraries."""
from src.domain.maze.entity.maze import Maze
from src.user_interface.component.maze_component import MazeComponent


def run():
    """Instantiate maze and render the maze component."""
    maze: Maze = Maze(7, 7, "Mac Gyver", "Guard", ['ether', 'needle', 'plastic_tube'])
    component: MazeComponent = MazeComponent(maze)
    component.render()


if __name__ == '__main__':
    run()

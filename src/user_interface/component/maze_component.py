"""Import libraries."""
import pygame
from pygame.sprite import Group

from src.domain.maze.entity.maze import Maze
from src.domain.maze.value_object.direction import Direction
from src.user_interface.component.cell_component import CellComponent
from src.user_interface.component.lose_component import LoseComponent
from src.user_interface.component.progress_component import ProgressComponent
from src.user_interface.component.win_component import WinComponent
from src.user_interface.sprite.enemy_sprite import EnemySprite
from src.user_interface.sprite.player_sprite import PlayerSprite


class MazeComponent:
    """
    MazeComponent.

    This component display the game with the maze in it,
    and group of sprites, like player and enemy.
    """

    def __init__(self, maze: Maze):
        """
        Create the pygame window.

        Add a group of sprite with player and enemy sprites.

        :param maze:
        """
        self.maze: Maze = maze
        pygame.init()
        self.window: pygame.Surface = pygame.display.set_mode(
            (
                (self.maze.x * 2 + 1) * 69,
                (self.maze.y * 2 + 1) * 49 + 50,
            )
        )
        self.player: PlayerSprite = PlayerSprite(self.maze.player)
        self.group: Group = pygame.sprite.Group()
        self.group.add(self.player)
        self.group.add(EnemySprite(self.maze.enemy))

    def render(self):
        """
        Display the maze.

        Rendering cell, player's progress and sprites (player and enemy).
        If the user use the escape key on his keyboard,
        then the game is over and the window is shutdown.
        If the user use a arrow key, then the player
        will move according to the direction of the key.
        if the player reaches the end of the game, the end popup is displayed.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT \
                        or (event.type == pygame.KEYDOWN
                            and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                elif not self.maze.player.finished \
                        and event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_UP:
                    self.player.move(Direction.UP)
                elif not self.maze.player.finished\
                        and event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_DOWN:
                    self.player.move(Direction.DOWN)
                elif not self.maze.player.finished\
                        and event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_LEFT:
                    self.player.move(Direction.LEFT)
                elif not self.maze.player.finished\
                        and event.type == pygame.KEYDOWN \
                        and event.key == pygame.K_RIGHT:
                    self.player.move(Direction.RIGHT)
                pass
            for cell in self.maze.cells:
                CellComponent(cell, self.window).render()

            ProgressComponent(self.maze, self.window).render()

            self.group.draw(self.window)

            if self.maze.player.finished:
                if self.maze.player.win:
                    WinComponent(self.window).render()
                if not self.maze.player.win:
                    LoseComponent(self.window).render()

            pygame.display.update()

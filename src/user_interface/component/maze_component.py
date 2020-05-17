import pygame
from pygame.sprite import Group

from src.domain.maze.entity.maze import Maze
from src.domain.maze.value_object.direction import Direction
from src.user_interface.component.cell_component import CellComponent
from src.user_interface.component.progress_component import ProgressComponent
from src.user_interface.sprite.enemy_sprite import EnemySprite
from src.user_interface.sprite.player_sprite import PlayerSprite


class MazeComponent:
    def __init__(self, maze: Maze):
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
            pygame.display.update()

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.sprite import Group

from config import CurrentPath
from src.domain.maze.entity.maze import Maze
from src.user_interface.sprite.backpack_item_sprite import BackpackItemSprite


class ProgressComponent:
    def __init__(self, maze: Maze, window: pygame.Surface):
        self.maze: Maze = maze
        self.window: pygame.Surface = window
        font = pygame.font.Font(
            CurrentPath + '/assets/fonts/Roboto-Regular.ttf',
            20
        )
        self.text: Font = font.render('Mac Gyver', True, (255, 255, 255))
        self.text_rect: Rect = self.text.get_rect()
        self.text_rect.topleft = (12, 6)
        self.group: Group = pygame.sprite.Group()
        x: int = 150
        for item in self.maze.player.items:
            self.item: BackpackItemSprite = BackpackItemSprite(item, x, 4)
            self.group.add(self.item)
            x += 50

    def render(self):
        self.window.blit(self.text, self.text_rect)
        self.group.draw(self.window)

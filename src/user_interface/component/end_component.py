import pygame

from abc import ABC, abstractmethod


class EndComponent(ABC):
    def __init__(self, window: pygame.Surface):
        self.window: pygame.Surface = window
        self.x = window.get_width() / 2 - 131
        self.y = window.get_height() / 2 - 150

    def render(self):
        self.window.blit(
            pygame.transform.scale(
                pygame.image.load(self.get_image()).convert_alpha(),
                (262, 300)
            ),
            (self.x, self.y),
            (0, 0, 262, 300)
        )

    @abstractmethod
    def get_image(self) -> str:
        pass

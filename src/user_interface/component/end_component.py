"""Import libraries."""
import pygame

from abc import ABC, abstractmethod


class EndComponent(ABC):
    """
    EndComponent.

    This component displays a simple image
    at the end of the game.
    """

    def __init__(self, window: pygame.Surface):
        """
        Define the position of the image.

        :param window:
        """
        self.window: pygame.Surface = window
        self.x = window.get_width() / 2 - 131
        self.y = window.get_height() / 2 - 150

    def render(self):
        """
        Add image in window.

        Display the image in window,
        by calling the abstract method get_image,
        who it's implementing in child classes.
        """
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
        """
        Return image.

        :return:
        """
        pass

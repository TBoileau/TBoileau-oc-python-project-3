"""Import libraries."""
from config import CurrentPath
from src.user_interface.component.end_component import EndComponent


class WinComponent(EndComponent):
    """
    WinComponent.

    This component, child of EndComponent,
    displays a simple image if the player
    win the game.
    """

    def get_image(self) -> str:
        """
        Return image.

        :return:
        """
        return CurrentPath + '/assets/img/win.png'

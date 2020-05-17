from config import CurrentPath
from src.user_interface.component.end_component import EndComponent


class WinComponent(EndComponent):
    def get_image(self) -> str:
        return CurrentPath + '/assets/img/win.png'

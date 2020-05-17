from src.user_interface.component.end_component import EndComponent


class LoseComponent(EndComponent):
    def get_image(self) -> str:
        return 'assets/img/lose.png'

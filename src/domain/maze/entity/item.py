from typing import Union, Any


class Item:
    def __init__(self, name: str, case):
        self.name: str = name
        self.case: Union[Any, None] = case

    def pick_up(self):
        self.case.remove_item()

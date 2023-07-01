from typing import Protocol


class GameCharacter(Protocol):

    def show_a_skill(self):
        ...

from dataclasses import dataclass

from game import factory


@dataclass
class CenaMember:

    name: str = "Fucking member"

    def show_a_skill(self):
        print(f"I'm {self.name} and I usually get salary for nothing.")


def register() -> None:
    factory.register('CenaMember', CenaMember)

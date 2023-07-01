from dataclasses import dataclass


@dataclass
class King:
    name: str

    def show_a_skill(self):
        print(f'My name is {self.name} and I watch the death of soldiers.')


@dataclass
class Soldier:

    name: str

    def show_a_skill(self):
        print(
            f'''My name is {self.name} and I kill myself with
            a grenade under a tank.
            '''
        )

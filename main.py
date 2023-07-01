import json

from game import factory
from game.characters import King, Soldier


def runner() -> None:

    factory.register("King", King)
    factory.register("Soldier", Soldier)

    with open('game_conf.json') as configuration:
        conf = json.loads(configuration.read())
        characters_conf_data = conf.get('characters')

        characters = [factory.create(character) for character in
                      characters_conf_data]

        for game_character in characters:
            print(game_character, end="\t")
            game_character.show_a_skill()


if __name__ == "__main__":
    runner()

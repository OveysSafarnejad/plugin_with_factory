from typing import Callable, Any

from game.protocol import GameCharacter

character_creators: dict[str, Callable[..., GameCharacter]] = {}


def register(
        game_character_type: str,
        creator: Callable[..., GameCharacter]
) -> None:
    character_creators[game_character_type] = creator


def unregister(game_character_type: str) -> None:
    character_creators.pop(game_character_type, None)


def create(arguments: dict[str: Any]) -> GameCharacter:
    args_copy = arguments.copy()
    character_type = args_copy.pop("type")
    try:
        creator_func = character_creators[character_type]
    except KeyError:
        raise ValueError(
            f"unknown character type {character_type!r}") from None
    return creator_func(**args_copy)

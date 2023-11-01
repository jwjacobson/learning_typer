# something seems to be broken here as it throws a TypeError, we'll just leave it for now

import random

import typer
from typing_extensions import Annotated


def get_animal():
    return random.choice(["bird", "monkey", "sasquatch", "goblin"])


def main(animal: Annotated[str, typer.Argument(default_factory=get_animal)]):
    print(f"It's a {animal}!")

if __name__ == "__main__":
    typer.run(main)


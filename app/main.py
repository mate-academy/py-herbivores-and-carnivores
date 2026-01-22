from __future__ import annotations
from typing import Iterator


class AliveList:
    def __init__(self) -> None:
        self.items: list[Animal] = []

    def __iter__(self) -> Iterator[Animal]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f"[{', '.join(f'{x!r}' for x in self.items)}]"

    def __getitem__(self, index: int) -> Animal:
        return self.items[index]

    def append(self, item: Animal) -> None:
        self.items.append(item)

    def remove(self, item: Animal) -> None:
        self.items.remove(item)


class Animal:
    alive: AliveList = AliveList()

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, \
Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50
                if animal.health <= 0:
                    Animal.alive.remove(animal)

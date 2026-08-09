from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health}, Hidden: {self.hidden}}}")

    def __getattribute__(self, name: str) -> list | Animal:
        if name == "alive":
            list_animals = []
            for animal in Animal.alive:
                list_animals.append(repr(animal))
            return list_animals
        return super().__getattribute__(name)


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore | Carnivore) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)

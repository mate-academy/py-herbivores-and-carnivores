from __future__ import annotations


class AnimalList(list["Animal"]):
    def __repr__(self) -> str:
        items = []
        for animal in self:
            items.append(
                f"{{Name: {animal.name}, "
                f"Health: {animal.health}, "
                f"Hidden: {animal.hidden}}}"
            )
        return "[" + ", ".join(items) + "]"


class Animal:
    alive: AnimalList = AnimalList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def remove_dead(cls, animal: "Animal") -> None:
        if animal in cls.alive:
            cls.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        target: "Herbivore",
    ) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                target.health = 0
                Animal.remove_dead(target)

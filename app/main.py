from typing import List, Union, Type


class Animal:
    alive: List["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def remove_dead(cls: Type["Animal"]) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    @classmethod
    def __str__(cls) -> str:
        return str([{"Name": animal.name,
                     "Health": animal.health,
                     "Hidden": animal.hidden}
                    for animal in cls.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Union[Animal, object]) -> None:
        if isinstance(target, Animal):
            if isinstance(target, Herbivore) and not target.hidden:
                target.health -= 50
        Animal.remove_dead()

from typing import Union

class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, target: Union[Animal, "Herbivore"]) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0 and target in Animal.alive:
                Animal.alive.remove(target)

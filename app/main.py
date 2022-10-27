from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{"f"Name: {self.name}, Health: {self.health}, "\
               f"Hidden: {self.hidden}""}"


class Herbivore(Animal):
    def hide(self) -> Herbivore:
        if self.hidden is True:
            self.hidden = False
        else:
            self.hidden = True
        return self


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.hidden is False and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            print("bited")
            if herbivore.health < 0 or herbivore.health == 0:
                herbivore.health = 0
                print(f"{herbivore.name} is dead")
        else:
            print(f"{self.name} cannot bite hidden {herbivore.name}")

        for animal in Animal.alive:
            if animal.health == 0:
                Animal.alive.remove(animal)

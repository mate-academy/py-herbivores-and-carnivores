from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str
                 , health: int = 100
                 , hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> Herbivore:
        self.hidden = not self.hidden
        return self


class Carnivore(Animal):
    def bite(self, an: Animal) -> None:
        if an.hidden or not isinstance(an, Herbivore):
            print(f"{self.name} cannot bite hidden {an.name}")
        else:
            an.health -= 50
            print("bited")
            if an.health <= 0:
                Animal.alive.remove(an)
                print(f"{an.name} is dead")

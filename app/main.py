from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive = Animal.alive
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herb: Herbivore | Carnivore) -> None:
        if isinstance(herb, Herbivore)\
                and herb.hidden is False:
            herb.health -= 50
        if herb.health <= 0:
            Animal.alive.remove(herb)
        else:
            print(f"{herb} is neither a Herbivore nor a Carnivore. Cannot bite.")

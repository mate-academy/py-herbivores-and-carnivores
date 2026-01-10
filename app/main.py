from __future__ import annotations


class Animal:
    alive = []

    def __init__(self
                 , name: str
                 , health: int = 100
                 , hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)


class Herbivore(Animal):
    def __init__(self
                 , name: str
                 , health: int = 100
                 , hidden: bool = False
                 ) -> None:
        super().__init__(name, health, hidden)

        if self.health <= 0:
            Animal.alive.remove(self)

    def hide(self):
        self.hidden = not self.hidden
        print(f"{self.name} is dead")


class Carnivores(Animal):
    def __init__(self
                 , name: str
                 , health: int = 100
                 , hidden: bool = False
                 ) -> None:
        super().__init__(name, health, hidden)

    @staticmethod
    def bite(animal: Herbivore) -> None:
        pass


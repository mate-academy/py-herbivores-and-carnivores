from __future__ import annotations


class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)
        Animal.check_alive(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, Hidden: "
                f"{self.hidden}}}")

    @staticmethod
    def check_alive(animal_obj: Animal) -> None:
        if animal_obj.health <= 0:
            if animal_obj in Animal.alive:
                Animal.alive.remove(animal_obj)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            herbivore: Herbivore
    ) -> None:

        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                if herbivore.health > 0:
                    herbivore.health -= 50
                    Animal.check_alive(herbivore)

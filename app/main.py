from __future__ import annotations


class Animal:

    alive = []

    def __repr__(self) -> str:
        result = "{"
        result_middle = f"Name: {self.name}, Health: {self.health}, "
        result_tail = f"Hidden: {self.hidden}" + "}"
        return result + result_middle + result_tail

    def __init__(self,
                 name: str,
                 health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def delete_from_alive(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(prey: Herbivore) -> None:
        if isinstance(prey, Herbivore):
            if not prey.hidden:
                prey.health -= 50
            if prey.health <= 0:
                prey.delete_from_alive()

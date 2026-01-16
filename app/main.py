from __future__ import annotations


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        name_str = f"Name: {self.name}"
        health_str = f"Health: {self.health}"
        hidden_str = f"Hidden: {self.hidden}"
        return f"{{{name_str}, {health_str}, {hidden_str}}}"

    @classmethod
    def remove_from_alive(cls, animal: Animal) -> None:
        cls.alive.remove(animal)

    def is_dead(self) -> bool:
        return self.health <= 0


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Carnivore) or prey.hidden or prey.is_dead():
            return

        prey.health -= 50
        if prey.is_dead():
            Animal.remove_from_alive(prey)

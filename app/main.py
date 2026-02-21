from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    # there is only one issue with __repr__ method
    # and how test_print_animal_alive accepts it
    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)


if __name__ == "__main__":
    pass

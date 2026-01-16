class Animal:
    alive = []

    def __init__(self, name: int, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, other: str) -> str | None:
        if not isinstance(other, Herbivore):
            return "invalid target"
        if other.hidden or other.health <= 0:
            return "target is hidden or dead"
        other.health -= 50
        if other.health <= 0:
            other.health = 0
            if other in Animal.alive:
                Animal.alive.remove(other)

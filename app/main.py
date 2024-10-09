class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        print(f"Animal __init__ called with: {name}, health: {health}")
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)
# Use

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health <= 0:
                other.die()

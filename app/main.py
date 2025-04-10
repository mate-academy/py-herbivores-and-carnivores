class Animal:

    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Animal) -> None:
        if isinstance(other, Herbivore):
            if other.hidden:
                print(f"{self.name} cannot bite hidden {other.name}")
            else:
                print(f"{self.name} bites {other.name}")
                other.health -= 50
                if other.health <= 0:
                    Animal.alive.remove(other)

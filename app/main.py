class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{"
            f"Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}"
            f"}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Carnivore):
            self.health = 100
        else:
            if not other.hidden:
                other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)

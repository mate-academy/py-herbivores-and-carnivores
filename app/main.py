class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        if health > 0:
            self.health = health
            self.name = name
            self.hidden = hidden
            Animal.alive.append(self)

    @classmethod
    def alive_attributes(cls) -> list:
        attributes = []
        for instance in cls.alive:
            attributes.append(instance.__dict__)
        return attributes

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other : Herbivore) -> None:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
        if other.health <= 0:
            other.health = 0
            Animal.alive.remove(other)

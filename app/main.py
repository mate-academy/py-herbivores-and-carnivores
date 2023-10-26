class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:

        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    @classmethod
    def remove_dead_animal(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

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
    def bite(self, other: Herbivore) -> None:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
            if other.health <= 0:
                Animal.remove_dead_animal()

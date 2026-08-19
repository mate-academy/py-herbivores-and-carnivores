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
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            other: Animal
    ) -> None:
        if other.hidden is False and isinstance(other, Carnivore) is False:
            other.health -= 50

        for animal in range(len(Animal.alive)):
            if other.health <= 0 and other == Animal.alive[animal]:
                del Animal.alive[animal]

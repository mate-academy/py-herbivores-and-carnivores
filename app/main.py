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
            harbivore_animal: "Herbivore"
    ) -> None:
        if (not isinstance(harbivore_animal, Carnivore)
                and not harbivore_animal.hidden):
            harbivore_animal.health -= 50
            if harbivore_animal.health <= 0:
                del Animal.alive[Animal.alive.index(harbivore_animal)]

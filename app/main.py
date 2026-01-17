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
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> dict:
        return (
            f"{{Name: {self.name}, "
            + f"Health: {self.health}, "
            + f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other_animal: Herbivore) -> None:
        if isinstance(other_animal, Herbivore) and not other_animal.hidden:
            other_animal.health -= 50
            if other_animal.health <= 0:
                Animal.alive.remove(other_animal)

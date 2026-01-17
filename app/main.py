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
            f"Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> bool:

        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(other_animal: "Herbivore") -> int | None:

        if isinstance(other_animal, Carnivore) or other_animal.hidden:
            return
        else:
            other_animal.health -= 50
            if other_animal.health <= 0:
                Animal.alive.remove(other_animal)

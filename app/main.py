class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int | float = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
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
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(
            self,
            animal: Animal
    ) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)

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
        return (f"{{"
                f"Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}"
                f"}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, some_animal: Animal) -> None:
        if isinstance(some_animal, Herbivore) and some_animal.hidden is False:
            some_animal.health -= 50
            if some_animal.health <= 0:
                Animal.alive.remove(some_animal)

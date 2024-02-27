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

    def update_status(self) -> None:
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)

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

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if (not herbivore.hidden
                and isinstance(herbivore, Herbivore)):
            herbivore.health -= 50
            herbivore.update_status()

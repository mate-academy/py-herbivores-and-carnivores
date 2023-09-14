class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int | None = 100,
            hidden: bool | None = False
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
    @staticmethod
    def bite(beast: Herbivore) -> None:
        if not beast.hidden and isinstance(beast, Herbivore):
            beast.health = beast.health - 50
            if beast.health <= 0:
                Animal.alive.remove(beast)

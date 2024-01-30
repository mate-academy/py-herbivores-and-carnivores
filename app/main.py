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

    def die(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}"
                f"}}"
                )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: "Herbivore") -> None:
        if not isinstance(herbivore, Herbivore) or herbivore.hidden:
            return
        herbivore.health -= 50
        herbivore.die()

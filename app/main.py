class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(
            self,
            beast: Animal
    ) -> None:
        if not isinstance(beast, Herbivore):
            return

        if beast.hidden:
            return

        beast.health -= 50

        if beast.health <= 0:
            beast.health = 0
            beast.die()

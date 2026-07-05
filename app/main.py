class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def check_health(self) -> None:
        if self.health <= 0:
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
    def bite(self, beast: Herbivore) -> None:
        if not isinstance(beast, Herbivore):
            return

        if beast.hidden:
            return

        beast.health -= 50
        beast.check_health()

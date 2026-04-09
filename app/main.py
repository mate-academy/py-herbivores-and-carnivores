class Animal:
    alive: list["Animal"] = []

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
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(
            self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            prey: Herbivore
    ) -> None:
        if not isinstance(prey, Herbivore):
            return
        if prey.hidden:
            return
        prey.health -= 50
        if prey.health <= 0 and prey in Animal.alive:
            Animal.alive.remove(prey)

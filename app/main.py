class Animal:
    alive: list["Animal"] = []

    def __init__(
        self: "Animal",
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden

        Animal.alive.append(self)

    def die(self: "Animal") -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self: "Animal") -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def __str__(cls: type) -> str:
        return str([
            {"Name": animal.name,
             "Health": animal.health,
             "Hidden": animal.hidden}
            for animal in cls.alive
        ])


class Herbivore(Animal):
    def hide(self: "Herbivore") -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(
        self: "Carnivore",
        prey: "Herbivore"
    ) -> None:

        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50

        if prey.health <= 0:
            prey.die()

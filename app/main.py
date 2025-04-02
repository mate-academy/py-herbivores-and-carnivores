class Animal:
    class _AliveList(list):
        def __repr__(self) -> str:
            return "[" + ", ".join(repr(animal) for animal in self) + "]"

    alive: "list[Animal]" = _AliveList()

    def __init__(
        self, name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> object:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def lose_health(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.lose_health(50)

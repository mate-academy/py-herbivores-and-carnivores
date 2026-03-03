class Animal:
    alive = []

    def __init__(
        self, name: str, health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{Name: " + str(self.name)
            + ", Health: " + str(self.health)
            + ", Hidden: " + str(self.hidden) + "}"
        )

    def _check_alive(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health <= 0:
            other.health = 0
        other._check_alive()

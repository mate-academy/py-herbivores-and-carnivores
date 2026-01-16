class Animal:
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __repr__(self) -> str:
        return str(self)

    def _die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        victim: Animal
    ) -> None:
        if not isinstance(victim, Herbivore):
            return
        if victim.hidden:
            return

        victim.health -= 50
        if victim.health <= 0:
            victim.health = 0
            victim._die()

class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __str__(self) -> str:
        return f"{self.name} (Health: {self.health})"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
            self,
            prey: object,
    ) -> bool:

        if prey is self or not isinstance(prey, Herbivore) or prey.hidden:
            return False

        prey.health -= 50

        if prey.health <= 0:
            prey.health = 0
            if prey in Animal.alive:
                Animal.alive.remove(prey)
            return True

        return False

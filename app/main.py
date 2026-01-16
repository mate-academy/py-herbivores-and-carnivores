class Animal():
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

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.die()


class Carnivore(Animal):
    def bite(
        self,
        prey: Animal
    ) -> None:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.take_damage(50)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

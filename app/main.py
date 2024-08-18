class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health: int = health
        self.name: str = name
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def decrease_health(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.__class__.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.decrease_health(50)

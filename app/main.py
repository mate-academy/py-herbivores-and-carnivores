class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if (
                isinstance(herbivore, Herbivore)
                and not herbivore.hidden
                and herbivore.health > 0
        ):
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)

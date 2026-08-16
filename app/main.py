class Animal:
    alive = []

    def __init__(self, name: str, hp: int = 100) -> None:
        self.name = name
        self.health = hp
        self.hidden = False
        Animal.alive.append(self)

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
    def bite(self, pray: Herbivore) -> None:
        if isinstance(pray, Herbivore) and not pray.hidden:
            pray.health -= 50

        if pray.health <= 0:
            Animal.alive.remove(pray)

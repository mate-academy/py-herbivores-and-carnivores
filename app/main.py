class Animal:
    hidden: bool = False
    alive: list = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbi: Herbivore) -> None:
        if not herbi.hidden and isinstance(herbi, Herbivore):
            herbi.health -= 50
            if herbi.health <= 0:
                Animal.alive.remove(herbi)

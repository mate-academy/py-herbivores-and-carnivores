class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: bool) -> list:
        if isinstance(herbivore, Carnivore) or herbivore.hidden:
            return
        herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)

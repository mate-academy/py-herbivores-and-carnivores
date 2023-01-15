class Animal:
    alive = list()

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        name = self.name
        health = self.health
        hidden = self.hidden
        return f"""{{Name: {name}, Health: {health}, Hidden: {hidden}}}"""


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)

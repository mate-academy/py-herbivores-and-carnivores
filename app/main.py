class Animal:
    hidden = False
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        name, health, hidden = self.name, self.health, self.hidden
        return f"{{Name: {name}, Health: {health}, Hidden: {hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not herbivore.hidden and not isinstance(herbivore, Carnivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                self.alive.remove(herbivore)

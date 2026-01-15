class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.hidden = False
        self.name = name

        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        animals_repr = (f"{{Name: {self.name}, "
                        f"Health: {self.health}, Hidden: {self.hidden}}}")
        return animals_repr


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, herbivore: str) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)

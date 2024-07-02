class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")
        # return result


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = not self.hidden
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if type(self) != type(herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
        if herbivore.health <= 0:
            self.alive.remove(herbivore)

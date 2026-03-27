class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self, *args, **kwargs) -> str:
        return "{" + (f"Name: {self.name}, "
                      f"Health: {self.health},"
                      f" Hidden: {self.hidden}") + "}"

    def __str__(self, *args, **kwargs) -> str:
        return str([alive.__repr__() for alive in Animal.alive])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.hidden is False and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.pop(Animal.alive.index(herbivore))

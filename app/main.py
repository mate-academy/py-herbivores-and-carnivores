class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return "{"f"Name: {self.name}, \
Health: {self.health}, \
Hidden: {self.hidden}""}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                super().alive.remove(herbivore)

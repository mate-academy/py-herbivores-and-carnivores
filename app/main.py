class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return "{{Name: {}, Health: {}, Hidden: {}}}".format(
            self.name, self.health, self.hidden
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Carnivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                super().alive.remove(herbivore)

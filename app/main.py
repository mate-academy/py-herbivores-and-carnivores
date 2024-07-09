class Animal:
    alive = []

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False)\
            -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Carnivore):
            return
        if herbivore.hidden is False:
            herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)

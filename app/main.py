class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100
                 ) -> None:

        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> bool:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Carnivore):
            return
        if herbivore.hidden:
            return

        herbivore.health -= 50

        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)

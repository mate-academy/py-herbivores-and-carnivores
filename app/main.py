class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        if health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        alive_animals = {
            "Name": self.name,
            "Health": self.health,
            "Hidden": self.hidden
        }

        return str(alive_animals).replace("'", "")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.hidden or isinstance(herbivore, Carnivore):
            return

        herbivore.health -= 50

        if herbivore.health <= 0:
            died_index = super().alive.index(herbivore)
            del super().alive[died_index]

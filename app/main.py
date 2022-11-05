class Animal:
    alive = []

    # {"Name": self.name, "Health": self.health, "Hidden": self.hidden} ----------------------------
    def __init__(self, name: str,
                 health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> None:
        print([{"Name": animal.name,
                "Health": animal.health, "Hidden": animal.hidden}
               for animal in Animal.alive])


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
                if herbivore.health <= 0:
                    Animal.alive.remove(herbivore)

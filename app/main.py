class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    @classmethod
    def __str__(cls) -> str:
        return str([{"Name": animal.name,
                     "Health": animal.health,
                     "Hidden": animal.hidden}
                    for animal in cls.alive])

    def __repr__(self) -> str:

        return (f"<Animal(name={self.name}, "
                f" health={self.health}, "
                f" hidden={self.hidden})>")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()

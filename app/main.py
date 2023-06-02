class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def remove_animal(self) -> None:
        if self in self.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        for _ in self.alive:
            return (f"{{Name: {self.name}, "
                    f"Health: {self.health}, "
                    f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health <= 0:
            herbivore.remove_animal()

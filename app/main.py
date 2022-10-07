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
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    @classmethod
    def viability(cls) -> None:
        for animal in cls.alive:
            if animal.health <= 0:
                cls.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
            self.viability()

class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return str(
            {key.capitalize(): value for key, value in self.__dict__.items()}
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if not self.hidden else False


class Carnivore(Animal):
    @classmethod
    def bite(cls, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
            if herbivore.health <= 0:
                cls.alive.remove(herbivore)

class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return str(self.__dict__).title().replace("'", "")

    @classmethod
    def get_alive(cls) -> list:
        return list([(repr(animal) for animal in cls.alive)])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health <= 0 and herbivore in Animal.alive:
            Animal.alive.remove(herbivore)

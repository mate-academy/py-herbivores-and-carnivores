class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.__hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f'{{Name: {self.name}, '
                f'Health: {self.health}, '
                f'Hidden: {self.__hidden}}}')

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    @property
    def hidden(self) -> bool:
        return self.__hidden

    @hidden.setter
    def hidden(self, value: bool) -> None:
        self.__hidden = value


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: "Herbivore") -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()

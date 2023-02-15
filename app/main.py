class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def die(self) -> None:
        self.__class__.alive.remove(self)


class Carnivore(Animal):
    def bite(self, herbivore: bool) -> None:
        if isinstance(herbivore, Carnivore) or herbivore.hidden:
            return
        herbivore.health -= 50
        if herbivore.health <= 0:
            herbivore.health = 0
            herbivore.die()


class Herbivore(Animal):
    def herb(self, name: str) -> None:
        super().__init__(name)

    def hide(self) -> None:
        self.hidden = not self.hidden

class AliveList(list):
    def __repr__(self) -> str:
        return "[" + ", ".join(repr(animal) for animal in self) + "]"


class Animal:
    alive = AliveList()

    def __init__(self, name: str, health: int = 100,) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def change_health(self, value: int) -> None:
        self.health = max(0, self.health - value)

        if self.health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Animal) -> None:
        if (
            isinstance(herbivore, Herbivore)
            and not herbivore.hidden
            and herbivore.health > 0
        ):
            herbivore.change_health(50)

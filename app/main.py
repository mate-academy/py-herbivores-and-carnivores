class AliveList(list):
    def __str__(self) -> str:
        return "[" + ", ".join(
            f"{{Name: {animal.name}, "
            f"Health: {animal.health}, "
            f"Hidden: {animal.hidden}}}"
            for animal in self
        ) + "]"


class Animal:
    alive = AliveList()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.__class__.alive.append(self)

    def update_health(self, health_shift: int) -> None:
        self.health += health_shift
        # check health changes
        # if below 0 - animal is dead
        if self.health <= 0:
            self.health = 0
            self.__class__.alive.remove(self)
        # if greater than 100 - set to 100 as its max health
        if self.health > 100:
            self.health = 100


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if type(other) is Herbivore:
            if not other.hidden:
                other.update_health(-50)

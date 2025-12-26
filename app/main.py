class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.alive.append(self)

    def __str__(self) -> str:
        return ("{" + f"Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}" + "}")

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        if isinstance(other, Carnivore) or other.hidden:
            return None
        other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)

class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.__health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        self.__health = value

        if self.__health <= 0:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(target: Herbivore) -> None:
        if not target.hidden and isinstance(target, Herbivore):
            target.health -= 50

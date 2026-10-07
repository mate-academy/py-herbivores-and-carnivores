class Animal:

    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.__health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, new_health: int) -> None:
        self.__health = new_health
        if new_health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50

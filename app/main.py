class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.__class__.alive.append(self)

    @staticmethod
    def check_is_alive() -> None:
        for animal in Animal.alive:
            if animal.health <= 0:
                Animal.alive.remove(animal)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            animal.check_is_alive()

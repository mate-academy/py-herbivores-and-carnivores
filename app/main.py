
class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

    @classmethod
    def reset_alive(cls) -> None:
        cls.alive = []

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = True if not self.hidden else False


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if not isinstance(animal, Herbivore):
            return
        if animal.hidden:
            return
        animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
            del animal

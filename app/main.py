
class Animal:

    alive = list()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{"
            + f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
            + "}"
        )

    def __str__(self) -> str:
        return Animal.alive


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = True if not self.hidden else False


class Carnivore(Animal):

    @classmethod
    def bite(cls, obj: Herbivore) -> None:
        for animal in super().alive:
            if (
                animal.name == obj.name
                and isinstance(animal, Herbivore)
                and not animal.hidden
            ):
                animal.health -= 50
            if animal.health <= 0:
                super().alive.remove(animal)

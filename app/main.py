class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore_object: Herbivore) -> None:
        if isinstance(herbivore_object, Herbivore) and \
                not herbivore_object.hidden:
            herbivore_object.health -= 50
            if herbivore_object.health <= 0:
                Animal.alive.remove(herbivore_object)

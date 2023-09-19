class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore_object: Herbivore) -> None:
        if isinstance(herbivore_object, Herbivore) and \
                herbivore_object.hidden is False:
            herbivore_object.health -= 50
            if herbivore_object.health <= 0:
                Animal.alive.remove(herbivore_object)

class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:

        name = f"Name: {self.name}"
        health = f"Health: {self.health}"
        hidden = f"Hidden: {self.hidden}"

        return f"{{{name}, {health}, {hidden}}}"


class Herbivore(Animal):

    def hide(self) -> bool:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Animal) -> None:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
            if prey.health <= 0:
                Animal.alive.remove(prey)

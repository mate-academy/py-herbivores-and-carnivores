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

        self.alive.append(self)

    def __repr__(self) -> str:

        name = f"Name: {self.name}"
        health = f"Health: {self.health}"
        hidden = f"Hidden: {self.hidden}"

        return f"{{{name}, {health}, {hidden}}}"


class Herbivore(Animal):

    def hide(self) -> bool:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, pray: Animal) -> None:
        if isinstance(pray, Herbivore) and pray.hidden is False:
            pray.health -= 50
            if pray.health <= 0:
                self.alive.remove(pray)

class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        self.alive.append(self)

    def __repr__(
            self
    ) -> str:
        return f"{{Name: {self.name}, Health: " \
               f"{self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(
            self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(
            pray: Animal
    ) -> None:
        if not (pray.hidden or isinstance(pray, Carnivore)):
            pray.health -= 50
            if pray.health <= 0:
                Animal.alive.remove(pray)

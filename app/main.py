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
        return f"{{" \
               f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def check_hp(self) -> None:
        if self.health <= 0:
            del Animal.alive[Animal.alive.index(self)]


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if (herbivore.hidden is False) and (isinstance(herbivore, Herbivore)):
            herbivore.health -= 50
        Herbivore.check_hp(herbivore)

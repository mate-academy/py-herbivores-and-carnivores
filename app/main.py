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
        self.alive.append(self)

    def is_dead(self) -> int:
        return self.health <= 0

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):

    def bite(self, beast: Animal) -> None:
        if isinstance(beast, Herbivore) and beast.hidden is False:
            beast.health -= 50
            if beast.is_dead():
                Animal.alive.remove(beast)

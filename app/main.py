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
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        setattr(self, "hidden", not self.hidden)


class Carnivore(Animal):

    def bite(self, aim: Herbivore) -> None:

        if isinstance(aim, Herbivore) and aim.hidden is True:
            aim.hidden -= 0
        if isinstance(aim, Herbivore) and aim.hidden is False:
            aim.health -= 50
            if aim.health <= 0:
                Animal.alive.remove(aim)

class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        elif self.hidden is True:
            self.hidden = False

        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Carnivore(Animal):
    @staticmethod
    def bite(beast: Herbivore) -> None:
        if isinstance(beast, Carnivore):
            pass
        if isinstance(beast, Herbivore):
            if beast.hidden is False:
                beast.health -= 50
                if beast.health <= 0:
                    Animal.alive.remove(beast)

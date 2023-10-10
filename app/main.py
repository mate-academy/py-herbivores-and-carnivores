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

    def __str__(self) -> str:
        return ("{" + f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}" + "}")


class Herbivore(Animal):
    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    def bite(self, herb: Herbivore) -> None:

        if type(herb) == Carnivore:
            pass
        elif not herb.hidden:
            herb.health -= 50

            if herb.health <= 0:
                super().alive.remove(herb)

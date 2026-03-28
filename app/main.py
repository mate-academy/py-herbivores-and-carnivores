class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:

        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return "{" + (f"Name: {self.name}, "
                      f"Health: {self.health}, "
                      f"Hidden: {self.hidden}") + "}"

    def check_alive(self) -> None:
        if self.health <= 0:
            self.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = self.hidden is not True


class Carnivore(Animal):

    @staticmethod
    def bite(victim: Herbivore) -> None:
        if isinstance(victim, Herbivore) and victim.hidden is False:
            victim.health -= 50
            victim.check_alive()

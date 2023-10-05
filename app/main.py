class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        self.alive.append(self)

    def __str__(self) -> None:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __repr__(self) -> None:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @classmethod
    def bite(cls, victim: Herbivore) -> None:
        if not isinstance(victim, Carnivore) and not victim.hidden:
            victim.health -= 50
            if not victim.health > 0:
                cls.alive.remove(victim)

class Animal:

    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:

        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @classmethod
    def bite(cls, victim: Herbivore) -> None:
        if not isinstance(victim, Carnivore) and not victim.hidden:
            victim.health -= 50
            if victim.health <= 0:
                cls.alive.remove(victim)

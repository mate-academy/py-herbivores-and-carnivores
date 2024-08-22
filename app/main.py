class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.hidden = hidden
        self.health = health
        self.alive.append(self)

    def __repr__(self) -> str:
        return ("{" + f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}" + "}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if victim.hidden is False and isinstance(victim, Herbivore):
            victim.health -= 50
            if victim.health < 1:
                Animal.alive.remove(victim)
        else:
            pass

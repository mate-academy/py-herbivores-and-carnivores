class Animal:
    alive = list()

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)

    def __repr__(self) -> str:
        return ("{" + f"Name: {self.name},"
                f" Health: {self.health}, Hidden: {self.hidden}" + "}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: Herbivore) -> None:
        if isinstance(victim, Herbivore) and victim.hidden is False:
            victim.health -= 50
            if victim.health < 1:
                Animal.alive.remove(victim)

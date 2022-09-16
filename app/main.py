class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: Animal) -> None:
        if not isinstance(victim, Carnivore) \
                and not victim.hidden:
            victim.health -= 50
        self.meat_grinder(victim)

    def meat_grinder(self, meat: Animal) -> None:
        if meat.health <= 0:
            Animal.alive.remove(meat)

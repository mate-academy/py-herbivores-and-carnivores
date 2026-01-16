class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return str({"Name": self.name,
                    "Health": self.health,
                    "Hidden": self.hidden}).replace("'", "")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(victim: Herbivore) -> None:
        if not victim.hidden and isinstance(victim, Herbivore):
            victim.health -= 50
            if victim.health <= 0:
                Animal.alive.remove(victim)

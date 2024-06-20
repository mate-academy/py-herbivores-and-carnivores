class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}"
                f"}}")

    def __str__(self) -> None:
        print(Animal.alive.__repr__())


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Animal) -> None:
        if isinstance(victim, Herbivore) and victim.hidden is False:
            victim.health -= 50
        if victim.health <= 0:
            victim.die()

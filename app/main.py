class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f'{{'
                f'Name: {self.name}, '
                f'Health: {self.health}, '
                f'Hidden: {self.hidden}}}')


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(other: "Animal") -> None:
        if not other.hidden and other.__class__ != Carnivore:
            other.health -= 50
        if other.health <= 0 and other in Animal.alive:
            Animal.alive.remove(other)

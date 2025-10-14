class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def cancel(self, other: int) -> None:
        self.health -= other
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(target: "Animal") -> None:

        if target.hidden is False and isinstance(target, Herbivore):
            target.health -= 50
            if target.health <= 0:
                target.health = 0
                Animal.alive.remove(target)

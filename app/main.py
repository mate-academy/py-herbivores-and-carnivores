class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        result = (f"{{Name: {self.name}, "
                  f"Health: {self.health}, "
                  f"Hidden: {self.hidden}}}")
        return f"{result}"


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(cls, victim: Animal) -> None:
        if not victim.hidden and victim.__class__ == Herbivore:
            victim.health -= 50
        if victim.health <= 0:
            Animal.alive.remove(victim)

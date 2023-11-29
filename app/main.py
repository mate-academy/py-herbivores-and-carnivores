class Animal:

    alive = []

    def __init__(self,
                 name: str,
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

    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden

    def died(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):

    @classmethod
    def bite(cls, herbivore_instance: "Herbivore") -> None:
        if isinstance(herbivore_instance, Herbivore):
            if herbivore_instance.hidden is False:
                herbivore_instance.health -= 50
            herbivore_instance.died()

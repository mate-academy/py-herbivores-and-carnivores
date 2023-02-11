class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if not self.hidden else False


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Animal) -> None:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
        if prey.health <= 0:
            Animal.alive.remove(prey)

class Animal:

    alive = []

    def __init__(self,
                 name: str = None,
                 health : int = 100,
                 hidden : bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if isinstance(self, Herbivore):
            self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(alive: Animal) -> None:
        if isinstance(alive, Herbivore) and alive.hidden is False:
            alive.health -= 50
        if alive.health <= 0:
            Animal.alive.remove(alive)

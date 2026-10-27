class Animal():

    alive = []

    def __init__(self,
                 name : str,
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

    @staticmethod
    def death(animal : "Animal") -> None:
        Animal.alive.remove(animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if not herbivore.hidden and not isinstance(herbivore, Carnivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.death(herbivore)

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
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal_herbivore: Herbivore) -> Herbivore:
        if animal_herbivore.hidden is False\
                and isinstance(animal_herbivore, Herbivore) is True:
            animal_herbivore.health -= 50
        for i in Animal.alive:
            if i.health <= 0:
                Animal.alive.remove(i)
        return animal_herbivore

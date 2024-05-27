class Animal:
    alive = []

    def __init__(self, name: str, health=100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Herbivore):
            return

        if herbivore.hidden is False:
            if herbivore.health == 100:
                herbivore.health = 50
            if herbivore.health == 50:
                Animal.die(herbivore)

        if herbivore.hidden is True:
            herbivore.health = 100


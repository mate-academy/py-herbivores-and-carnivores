class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100):
        self.name = name
        self.health = health
        self.hidden = False

        if self.health > 0:
            Animal.alive.append(self)

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal):
        if not isinstance(animal, Herbivore):
            return
        if animal.hidden:
            return
        if animal.health <= 0:
            return

        animal.health -= 50

        if animal.health <= 0:
            animal.health = 0
            animal.die()

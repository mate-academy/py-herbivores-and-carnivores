class Animal:
    alive = []

    def __init__(self, name, health=100, hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

        if self.health <= 0:
            self.health = 0
            self.die()

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal) -> None:
        # не працює, якщо це інший хижак або взагалі не травоїдний
        if isinstance(animal, Carnivore) or not isinstance(animal, Herbivore):
            return

        # не працює, якщо травоїдна тварина ховається
        if animal.hidden:
            return

        animal.health -= 50

        if animal.health <= 0:
            animal.health = 0
            animal.die()

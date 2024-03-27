class Animal:
    alive = []

    def __init__(self, health=100, name="", hidden=False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def decrease_health(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self):
        Animal.alive.remove(self)


class Herbivore(Animal):
    def __init__(self, name):
        super().__init__(name=name)

    def hide(self):
        self.hidden = not self.hidden
class Carnivore(Animal):
    def __init__(self, name):
        super().__init__(name=name)

    @staticmethod
    def bite(animal):
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.decrease_health(50)


pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)

class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive.append(self)

    def __repr__(self):
        for animal in self.alive:
            dictionary = f"'Name': {self.name}, 'Health': {self.health}, 'Hidden': {self.hidden}"
            return dictionary


class Herbivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    @staticmethod
    def bite(instance) -> None:
        if instance.hidden is False:
            instance.health -= 50
        if instance.health == 0:
            Animal.alive.remove(instance)


rabbit = Herbivore("Susan")
lion = Carnivore("Lion King")
print(rabbit.health)
lion.bite(rabbit)
print(rabbit.health)
rabbit.hide()
lion.bite(rabbit)
print(rabbit.health)
rabbit.hide()
lion.bite(rabbit)
print(rabbit.health)
print(rabbit in Animal.alive)
snake = Carnivore("Kaa")
print(Animal.alive)

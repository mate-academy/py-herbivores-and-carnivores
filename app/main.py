class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive.append(self)

    # def alive(self):
    #     return Animal.alive.__dict__


class Herbivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def bite(self) -> None:
        if self.hidden is False:
            self.health -= 50


rabbit = Herbivore("Susan")
lion = Carnivore("Lion King")
print(rabbit.health)
lion.bite(rabbit)
print(rabbit.health)
print(Animal.alive)
print(rabbit in Animal.alive)

# # rabbit.hide()
# print(rabbit.hidden) #is True
# class Carnivore(Animal):

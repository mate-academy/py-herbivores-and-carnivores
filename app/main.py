class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
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
        if self.hidden:
            self.hidden = False
        elif not self.hidden:
            self.hidden = True


class Carnivore(Animal):

    def bite(self, animal: Herbivore) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)

# lion = Carnivore("King Lion")
# pantera = Carnivore("Bagira")
# rabbit = Herbivore("Susan")
# print(Animal.alive)
# lion.bite(rabbit)

#
# lion = Carnivore("Lion King")
# rabbit = Herbivore("Susan")
# # print(Animal.alive[1].name)
# Animal.alive.remove(lion)
# print(Animal.alive[0].name)
# # print(rabbit.health)
# lion.bite(rabbit)
# print(rabbit.health)
#
# rabbit.to_hide()
# lion.bite(rabbit)
# # print(rabbit.health)
#
#
# rabbit.to_hide()
# lion.bite(rabbit)
# print(rabbit.health)
#
# print(rabbit in Animal.alive)

# pantera = Carnivore("Bagira")
# snake = Carnivore("Kaa")
# print(pantera)
# print(Animal.alive)

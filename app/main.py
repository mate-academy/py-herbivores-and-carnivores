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

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Herbivore) -> None:
        if not animal.hidden and not isinstance(animal, Carnivore):
            animal.health -= 50

        if animal.health <= 0:
            Animal.alive.remove(animal)


# lion = Carnivore("Lion King")
# rabbit = Herbivore("Susan")
# print(rabbit.health == 100)
# lion.bite(rabbit)
# print(rabbit.health == 50) # bited
#
# rabbit.hide()
# lion.bite(rabbit)
# print(rabbit.health == 50)  # lion cannot bite hidden rabbit
#
# rabbit.hide()
# lion.bite(rabbit)
# print(rabbit.health == 0)  # rabbit is dead
#
# print(Animal.alive)
# print(Animal)

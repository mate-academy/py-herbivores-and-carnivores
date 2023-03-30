class Animal:
    health = 100
    hidden = False
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        if self.health > 0:
            self.alive.append({self})

    def __repr__(self) -> str:
        return print(f"{{Name: {self.name},"
                     f"Health: {self.health},"
                     f"Hidden_atribute: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

        return self.hidden

class Carnivore(Animal):

    @staticmethod
    def bite(animal: Animal):
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)

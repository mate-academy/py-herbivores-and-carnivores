class Animal:
    alive = []
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        self.alive.append(self)


    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if not isinstance(animal, Carnivore):
            if not animal.hidden:
                animal.health -= 50
                if animal.health <= 0:
                    Animal.alive.remove(animal)
                    del animal


# pantera = Carnivore("Bagira")
# snake = Carnivore("Kaa")
# print(Animal.alive)
class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.add_alive_animal()

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, Hidden: {self.hidden}}}"

    def add_alive_animal(self) -> None:
        if self.health > 0:
            Animal.alive.append(self)

    def remove_dead_animal(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if animal.hidden is not True and isinstance(animal, Herbivore):
            animal.health -= 50
            print(self.name, "health =", self.health)
            animal.remove_dead_animal()

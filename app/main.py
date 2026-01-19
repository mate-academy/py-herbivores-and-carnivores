class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health : int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        if self.health <= 0:
            return
        else:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name:"
                f" {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if not isinstance(animal, Herbivore):
            return
        if animal.hidden:
            return
        animal.health -= 50
        if animal.health <= 0:
            animal.die()

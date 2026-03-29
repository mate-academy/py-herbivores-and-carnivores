class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
        return (
            "{Name: "
            f"{self.name}, Health: {self.health}, Hidden: {self.hidden}"
            "}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore) or animal.hidden:
            return

        animal.health -= 50
        if animal.health <= 0 and animal in Animal.alive:
            Animal.alive.remove(animal)

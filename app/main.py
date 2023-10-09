class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if (animal.hidden or animal not in animal.alive
                or not isinstance(animal, Herbivore)):
            return
        animal.health -= 50
        if animal.health <= 0:
            for item in Animal.alive:
                if item.name == animal.name:
                    Animal.alive.remove(item)

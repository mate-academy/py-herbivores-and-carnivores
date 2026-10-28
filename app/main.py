class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self) if health > 0 else None

    def __str__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __repr__(self) -> str:
        return self.__str__()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore):
            return
        if animal.hidden:
            return
        else:
            animal.health -= 50
            Animal.alive.remove(animal) if animal.health <= 0 else None

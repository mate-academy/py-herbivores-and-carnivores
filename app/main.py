class Animal:
    alive = list()

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        animal = (f"{{Name: {self.name}, Health: {self.health},"
                  f" Hidden: {self.hidden}}}")
        return animal


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, another_animal: Animal) -> None:
        if not another_animal.hidden and isinstance(another_animal, Herbivore):
            another_animal.health -= 50
            if another_animal.health < 1:
                Animal.alive.remove(another_animal)

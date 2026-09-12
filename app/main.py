class Animal:
    alive = []

    def __init__(self, name: str, health: int | None = None) -> None:
        self.name = name
        self.health = health if health is not None else 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if animal.hidden:
            return
        if not isinstance(animal, Herbivore):
            return
        animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)

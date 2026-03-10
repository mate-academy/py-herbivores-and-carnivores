class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, " f"Hidden: {self.hidden}}}"
        )

    @staticmethod
    def alive() -> list[str]:
        return [repr(animal) for animal in Animal.alive]


class Herbivore(Animal):
    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        super().__init__(name, health, hidden)

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        super().__init__(name, health, hidden)

    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Carnivore):
            return
        if not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)

class Animal:
    alive: list["Animal"] = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.add_animal(self)

    @classmethod
    def add_animal(cls, animal: "Animal") -> None:
        cls.alive.append(animal)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            Animal.alive = [
                animal for animal in Animal.alive
                if animal is not self
            ]

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.take_damage(50)

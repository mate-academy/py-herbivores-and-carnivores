class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def remove_dead(cls, dead_animal: "Animal") -> None:
        cls.alive = [animal for animal in cls.alive if animal != dead_animal]


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: "Animal") -> None:
        if not isinstance(herbivore, Carnivore) and not herbivore.hidden:
            herbivore.health -= 50
            Animal.remove_dead(herbivore)

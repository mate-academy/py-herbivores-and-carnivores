class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def get_alive(cls) -> list:
        return [repr(animal) for animal in cls.alive]


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(second_animal: Herbivore) -> int:
        if (isinstance(second_animal, Herbivore)
                and not second_animal.hidden):
            second_animal.health -= 50
            if second_animal.health <= 0:
                Animal.alive.remove(second_animal)
        return second_animal.health

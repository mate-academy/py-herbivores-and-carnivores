class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}"
                f", Health: {self.health}"
                f", Hidden: {self.hidden}}}")


class Carnivore(Animal):
    @staticmethod
    def bite(other_animal: Animal) -> None:
        if isinstance(other_animal, Herbivore) and not other_animal.hidden:
            other_animal.health -= 50
            if other_animal.health <= 0:
                Animal.alive.remove(other_animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

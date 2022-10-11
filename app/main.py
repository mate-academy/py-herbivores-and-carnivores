class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {False}}}"


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: str) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)

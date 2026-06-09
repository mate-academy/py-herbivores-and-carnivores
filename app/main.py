class Animal:
    alive = []

    def __init__(
        self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        body = ", ".join(
            f"{key.capitalize()}: {value}"
            for key, value in self.__dict__.items()
        )
        return "{" + body + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                index_to_pop = Animal.alive.index(animal)
                Animal.alive.pop(index_to_pop)

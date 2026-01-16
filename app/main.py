class Animal:
    alive = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def remove_dead(cls: type) -> None:
        cls.alive = [
            animal
            for animal in cls.alive
            if animal.health > 0
        ]

    @classmethod
    def __str__(cls: type) -> str:
        return str(cls.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            Animal.remove_dead()

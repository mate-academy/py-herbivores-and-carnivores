class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )

    @classmethod
    def check_alive(cls) -> None:
        cls.alive = [animal for animal in cls.alive if animal.health > 0]

    def die(self) -> None:
        if self.health <= 0:
            Animal.check_alive()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            herbivore.die()

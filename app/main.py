class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @staticmethod
    def check_alive_animals() -> None:
        Animal.alive = [animal for animal in Animal.alive if animal.health > 0]

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
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50
            Animal.check_alive_animals()

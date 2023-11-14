class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @staticmethod
    def is_alive() -> None:
        for animal in Animal.alive:
            if animal.health <= 0:
                Animal.alive.remove(animal)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
        Animal.is_alive()

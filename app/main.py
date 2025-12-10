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
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def check_is_alive(self) -> bool:
        return self.health <= 0 and self in Animal.alive


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herb: Herbivore) -> None:
        if isinstance(herb, Herbivore) and not herb.hidden:
            herb.health -= 50
            if herb.check_is_alive():
                Animal.alive.remove(herb)

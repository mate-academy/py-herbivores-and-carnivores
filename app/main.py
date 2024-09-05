class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False)\
            -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> str:
        return self.alive.__repr__()

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: "
                f"{self.health}, Hidden: {self.hidden}}}")

    def get_bit(self) -> None:
        self.health -= 50
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.get_bit()

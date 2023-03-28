class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> any:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Animal) -> any:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
        if other.health <= 0:
            Animal.alive.remove(other)

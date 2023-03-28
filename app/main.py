class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> any:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __str__(self) -> str:
        return str([
            {"Name": animal.name, "Health": animal.health,
             "Hidden": animal.hidden}
            for animal in Animal.alive
        ])


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: Animal) -> any:
        if not other.hidden and isinstance(other, Herbivore):
            other.health -= 50
        if other.health <= 0:
            Carnivore.alive.remove(other)

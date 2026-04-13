class Animal:
    alive = []
    def __init__(self, name: str, health=100, hidden=False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: any) -> None:
        if not other.hidden and not isinstance(other, Carnivore):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)
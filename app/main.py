class Animal:
    alive = []
    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Carnivore):
            return
        if other.hidden:
            return
        other.health -= 50
        if other.health <= 0 and other in Animal.alive:
            Animal.alive.remove(other)

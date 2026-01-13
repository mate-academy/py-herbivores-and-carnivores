class Animal:
    alive = []

    def __init__(self, name, health = 100, hidden = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, other) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
        if isinstance(other, Herbivore):
            if other.health <= 0:
                if other in Animal.alive:
                    Animal.alive.remove(other)

class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def take_damage(self, amount: int) -> None:
        self.health = max(self.health - amount, 0)
        if self.health == 0 and self in Animal.alive:
            Animal.alive.remove(self)

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if not isinstance(target, Herbivore) or target.hidden or target.health == 0:
            return
        target.take_damage(50)

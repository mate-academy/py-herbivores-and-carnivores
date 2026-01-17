class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def set_health(self, health: int) -> None:
        self.health = health
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.set_health(target.health - 50)

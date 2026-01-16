class Animal:
    alive = []  # Class attribute to track all alive animals

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def is_alive(self) -> bool:
        return self.health > 0

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden  # Toggle the hidden status


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if (isinstance(herbivore, Herbivore)
                and not herbivore.hidden
                and herbivore.is_alive()):
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()

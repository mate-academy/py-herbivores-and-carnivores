class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        # Prevent duplicate registration
        if self not in Animal.alive:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    __str__ = __repr__


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: "Herbivore") -> None:
        if hasattr(herbivore, "hide") and not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health <= 0 and herbivore in Animal.alive:
            Animal.alive.remove(herbivore)

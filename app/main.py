class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, other: "Animal") -> int:
        if isinstance(other, Herbivore) and other.hidden is False:
            other.health -= 50
        if other.health <= 0 and other in Animal.alive:
            Animal.alive.remove(other)
        return other.health

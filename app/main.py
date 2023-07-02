class Animal:
    health = 100
    hidden = False
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.alive.append(self)

    def __repr__(self) -> str:
        for animal in self.alive:
            return "{" \
                f"Name: {self.name}, " \
                f"Health: {self.health}, " \
                f"Hidden: {self.hidden}" \
                "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: "Animal") -> None:
        if isinstance(other, Carnivore):
            return

        if other.hidden:
            return

        other.health -= 50

        if other.health <= 0:
            Animal.alive.remove(other)

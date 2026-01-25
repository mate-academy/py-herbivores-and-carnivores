
class Animal:
    alive = []

    def __init__(
        self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        parts = [
            f"Name: {self.name}",
            f"Health: {self.health}",
            f"Hidden: {self.hidden}",
        ]
        return "{" + ", ".join(parts) + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victum: Herbivore) -> None:
        if not isinstance(victum, Herbivore):
            return
        if victum.hidden:
            return

        victum.health -= 50
        if victum.health <= 0 and victum in Animal.alive:
            Animal.alive.remove(victum)

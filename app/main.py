class Animal:
    alive = []

    def __init__(
        self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: str) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                target.die()

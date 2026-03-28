class Animal:
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        # Exact format expected by the tests (no quotes around keys)
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        # Only bite herbivores that are not hidden
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return
        target.health -= 50
        if target.health <= 0:
            target.health = 0
            target.die()

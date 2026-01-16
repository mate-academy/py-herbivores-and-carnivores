class Animal:

    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, target: "Herbivore") -> None:
        if isinstance(target, Herbivore):
            if target.health > 0 and not target.hidden:
                target.health = max(0, target.health - 50)
        if target.health == 0 and target in Animal.alive:
            Animal.alive.remove(target)

class Animal:
    alive = []

    def __init__(
        self, name: str, health: int = 100, hiden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hiden
        if self not in Animal.alive:
            Animal.alive.append(self)

    def __str__(self) -> str:
        return f"Name: {self.name} Health: {self.health}"

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: object) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                if target in Animal.alive:
                    Animal.alive.remove(target)
                del target

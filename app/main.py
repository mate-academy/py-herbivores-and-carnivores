class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return ("{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}"
                "}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if is_herbivore(prey) and not prey.hidden:
            prey.health -= 50
        if prey.health <= 0:
            Animal.alive.remove(prey)


def is_herbivore(animal: any) -> bool:
    return isinstance(animal, Herbivore)

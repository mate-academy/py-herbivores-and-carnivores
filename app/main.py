class Animal:
    # registry of alive animals
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    # Magic method to control how the object displays inside a list
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

    def bite(self, target: Herbivore) -> None:
        if isinstance(target, Herbivore):
            if target in Animal.alive:
                if not target.hidden:
                    target.health -= 50
                    if target.health <= 0:
                        Animal.alive.remove(target)

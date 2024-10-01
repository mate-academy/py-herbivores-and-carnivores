class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name},"
            f"Health: {self.health},"
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self.health <= 0:
            self.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden

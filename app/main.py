class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden_atr: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden_atr
        Animal.alive.append(self)

    def death(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}"
        )

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
    def bite(self, herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.death()

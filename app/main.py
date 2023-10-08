class Animal:
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
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50

            if herbivore.health <= 0:
                cls.alive.remove(herbivore)

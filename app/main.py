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
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, "\
            f"Health: {self.health}, "\
            f"Hidden: {self.hidden}}}"

    def __len__(self) -> int:
        return len([animal for animal in self.alive if animal.health > 0])


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health <= 0:
            self.alive.remove(herbivore)

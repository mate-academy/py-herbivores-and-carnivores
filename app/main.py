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
        list_animal = []
        list_animal.append(f"{{"
                           f"Name: {self.name}, "
                           f"Health: {self.health}, "
                           f"Hidden: {self.hidden}}}")
        return ", ".join(list_animal)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, other: Herbivore) -> None:
        if (
                isinstance(self, Carnivore)
                and isinstance(other, Herbivore)
                and other.hidden is False
        ):
            other.health -= 50
            if other.health <= 0:
                Animal.alive.remove(other)

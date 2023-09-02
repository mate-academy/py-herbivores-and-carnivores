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
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Carnivore(Animal):
    @staticmethod
    def bite(herb_animal: Animal) -> None:
        if herb_animal.hidden is False and isinstance(herb_animal, Herbivore):
            herb_animal.health -= 50
            if herb_animal.health <= 0:
                Animal.alive.remove(herb_animal)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

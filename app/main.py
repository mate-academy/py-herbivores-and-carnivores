class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore_animal: Herbivore) -> None:
        if not isinstance(herbivore_animal, Carnivore):
            if not herbivore_animal.hidden:
                herbivore_animal.health -= 50
        if herbivore_animal.health <= 0:
            Animal.alive = [animal
                            for animal in Animal.alive
                            if animal.name != herbivore_animal.name
                            ]

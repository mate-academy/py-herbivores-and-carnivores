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
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(bitten_animal: "Animal") -> None:
        if isinstance(bitten_animal, Carnivore):
            return
        if bitten_animal.hidden:
            return
        bitten_animal.health -= 50
        if bitten_animal in Animal.alive:
            bitten_animal_index = Animal.alive.index(bitten_animal)
            if bitten_animal.health <= 0:
                Animal.alive.pop(bitten_animal_index)

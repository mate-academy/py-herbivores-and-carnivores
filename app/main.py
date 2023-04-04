class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, bitten_animal: Animal) -> None:
        if isinstance(bitten_animal, Herbivore):
            if bitten_animal.hidden:
                print(f"{self.name} cannot bite hidden {bitten_animal.name}")
            else:
                bitten_animal.health -= 50

        if bitten_animal.health <= 0:
            Animal.alive.remove(bitten_animal)

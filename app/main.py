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

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):

    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False

class Carnivore(Animal):

    def bite(self, herb_animal: Herbivore):
        if not herb_animal.hidden:
            if isinstance(herb_animal, Herbivore):
                herb_animal.health -= 50
                if herb_animal.health <= 0:
                    Animal.alive.remove(herb_animal)

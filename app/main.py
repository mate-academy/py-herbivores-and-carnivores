class Animal:
    alive = []

    def __init__(self, name: str,
                 health : int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    @staticmethod
    def list_alive_animals() -> str:
        return ", ".join(str(animal.to_dict()) for animal in Animal.alive)

    def to_dict(self) -> dict:
        return {"Name": self.name,
                "Health": self.health,
                "Hidden": self.hidden}


class Herbivore(Animal):

    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, herbivore_animal: Herbivore) -> None:
        if isinstance(herbivore_animal, Herbivore):
            if not herbivore_animal.hidden:
                herbivore_animal.health -= 50

            if herbivore_animal.health <= 0:
                Animal.alive.remove(herbivore_animal)

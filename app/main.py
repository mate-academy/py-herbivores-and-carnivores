class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return str(
            {"Name": self.name,
             "Health": self.health,
             "Hidden": self.hidden
             }
        ).replace("'", "")


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50
                if animal.health <= 0:
                    Animal.alive.remove(animal)

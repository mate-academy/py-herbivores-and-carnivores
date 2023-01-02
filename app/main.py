class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return "{" + f"Name: {self.name}, Health: {self.health}," \
                     f" Hidden: {self.hidden}" + "}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):
    @staticmethod
    def bite(other_animal: Animal) -> None:
        if isinstance(other_animal, Herbivore) and \
                other_animal.hidden is False:
            other_animal.health -= 50
        if other_animal.health <= 0:
            Animal.alive.remove(other_animal)

class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        if len(Animal.alive) > 0:
            if all(not isinstance(a, Animal) for a in Animal.alive):
                Animal.alive.clear()

        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def change_health(self, delta_health: int) -> None:
        if isinstance(delta_health, int):
            self.health += delta_health
            if self.health <= 0:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Animal) -> None:
        if isinstance(herbivore, Animal) and not herbivore.hidden:
            if isinstance(herbivore, Herbivore):
                herbivore.change_health(-50)

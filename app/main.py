class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        Animal.alive.append(self)
        self.hidden = False
        self.health = health

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Animal) -> None:
        if not prey.hidden and isinstance(prey, Herbivore):
            if prey.health < 50:
                prey.health = 0
            else:
                prey.health -= 50
        if prey.health <= 0:
            Animal.alive.remove(prey)

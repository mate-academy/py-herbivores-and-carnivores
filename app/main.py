class Animal:
    alive: list["Animal"] = []

    def __init__(self, name: str = "", health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def change_health(self, amount: int) -> None:
        self.health += amount
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if prey.health > 0:
            if not prey.hidden and not isinstance(prey, Carnivore):
                prey.change_health(-50)

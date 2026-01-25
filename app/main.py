class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health:
                 int = 100,
                 hidden: bool = False) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def reduce_health(self, amount: int) -> None:
        self.health = max(self.health - amount, 0)
        if self.health == 0:
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}"
                f", Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if not isinstance(target, Herbivore):
            return
        if target.hidden:
            return
        target.reduce_health(50)

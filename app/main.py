class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def get_bitten(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.perish()

    def perish(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @classmethod
    def alive_list_repr(cls) -> str:
        return f"[{", ".join([repr(animal) for animal in cls.alive])}]"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Herbivore) -> None:
        if isinstance(prey, Herbivore):
            if not prey.hidden:
                prey.get_bitten(50)

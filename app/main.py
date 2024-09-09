class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 alive: bool = True,
                 hidden: bool = False) -> None:
        self.alive = alive
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f" Hidden: {self.hidden}}}")

    def bitten(self) -> None:
        self.health -= 50
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Herbivore) -> None:
        if not victim.hidden and isinstance(victim, Herbivore):
            victim.bitten()

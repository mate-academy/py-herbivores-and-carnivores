class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def hide(self) -> None:
        self.hidden = not self.hidden

    def bitten(self) -> None:
        if self.hidden:
            return

        self.health -= 50
        if not self.is_alive:
            self.alive.remove(self)


class Carnivore(Animal):
    def bite(self, animal: Herbivore):
        animal.bitten()

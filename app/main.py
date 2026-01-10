class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)


class Herbivore(Animal):
    def __init__(self, name: str, health: int = 100, hidden: bool = False) -> None:
        super().__init__(name, health, hidden)

    def hide(self):
        self.hidden = True



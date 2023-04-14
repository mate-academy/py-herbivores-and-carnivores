class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def is_dead(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)

    def hidden_switcher(self) -> None:
        self.hidden = not self.hidden


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden_switcher()


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if not herbivore.hidden:
                herbivore.health -= 50
                herbivore.is_dead()

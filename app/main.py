class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.alive.append(self)
        # where to add instances to Animal.alive?

    def print_info(self) -> None:
        for item in self.alive:
            print(
                f"Name: {item.name}, "
                f"Health: {item.health}, "
                f"Hidden: {item.hidden}"
            )


class Herbivore(Animal):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health, hidden)

    @classmethod
    def hide(cls) -> None:
        cls.hidden = True


class Carnivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    @classmethod
    def bite(cls, herbivore: Herbivore) -> None:
        if Herbivore and Herbivore.hidden is False:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)

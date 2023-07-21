class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

    def print_info(self) -> None:
        for item in self.alive:
            print(f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}")


class Herbivore(Animal):
    def __init__(self, name: str, health: int):
        super().__init__(self, name, health, hidden)

    def hide(self):
        self.hidden = True


class Carnivore(Animal):
    def __init__(self, name: str, health: int):
        super().__init__(self, name, health, hidden)

    @staticmethod
    def bite(self, herbivore: Herbivore):
        if Herbivore and Herbivore.hidden is False:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)

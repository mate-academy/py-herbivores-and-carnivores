class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def is_dead(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Carnivore(Animal):
    @staticmethod
    def bite(prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
            prey.is_dead()

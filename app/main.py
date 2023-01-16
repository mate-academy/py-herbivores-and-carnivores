class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        self.__class__.alive.append(self)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(status: Herbivore) -> None:
        if isinstance(status, Herbivore) and not status.hidden:
            status.health -= 50

        if status.health <= 0:
            Animal.alive.remove(status)

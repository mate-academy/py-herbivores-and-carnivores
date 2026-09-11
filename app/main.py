
class Animal:
    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def kill_if_0(self) -> None:
        if self.health <= 0:
            self.alive.remove(self)

    alive = []

    def __repr__(self) -> str:

        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = True if not self.hidden else False


class Carnivore(Animal):

    @staticmethod
    def bite(animal : Animal) -> None:

        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50

        animal.kill_if_0()

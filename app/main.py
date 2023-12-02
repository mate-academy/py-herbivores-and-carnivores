class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def check_is_alive(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = False if self.hidden is True else True


class Carnivore(Animal):

    @staticmethod
    def bite(another_beast: Animal) -> None:
        if not (isinstance(another_beast, Carnivore) or another_beast.hidden):
            another_beast.health -= 50
            another_beast.check_is_alive()

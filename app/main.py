class Animal:

    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    @staticmethod
    def is_dead(lunch_name: str) -> None:
        if lunch_name.health <= 0:
            Animal.alive.remove(lunch_name)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, lunch_name: str) -> None:
        if isinstance(lunch_name, Herbivore) and lunch_name.hidden is False:
            lunch_name.health -= 50
            self.is_dead(lunch_name)

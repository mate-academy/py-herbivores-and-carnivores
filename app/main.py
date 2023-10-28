class Animal:

    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        for _ in Animal.alive:
            return f"{{" \
                   f"Name: {self.name}, " \
                   f"Health: {self.health}, " \
                   f"Hidden: {self.hidden}" \
                   f"}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(beast: Herbivore) -> None:
        if beast.hidden is False and isinstance(beast, Herbivore):
            beast.health -= 50
            if beast.health <= 0:
                Animal.alive.remove(beast)

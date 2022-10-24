class Animal:
    alive = list()

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        self.__class__.alive.append(self)

    def __repr__(self) -> str:
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
    def bite(biter: Herbivore) -> None:
        if isinstance(biter, Herbivore) and not biter.hidden:
            biter.health -= 50
        if biter.health <= 0:
            biter.alive.remove(biter)

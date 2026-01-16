class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return f"{{Name: {self.name}, Health:" \
               f" {self.health}, Hidden: {self.hidden}}}"

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: str) -> None:
        if isinstance(herbivore, Carnivore) or herbivore.hidden:
            return
        herbivore.health -= 50
        if herbivore.health <= 0:
            herbivore.die()

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
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"

    def set_health(self, health: int) -> None:
        self.health = health

    def is_hidden(self) -> bool:
        return self.hidden

    def is_dead(self) -> bool:
        return self.health <= 0


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.is_hidden():
            herbivore.health -= 50
            if herbivore.is_dead():
                Animal.alive.remove(herbivore)

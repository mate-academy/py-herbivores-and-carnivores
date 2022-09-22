class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        name, health, hidden = self.name, self.health, self.hidden
        return f"{{Name: {name}, Health: {health}, Hidden: {hidden}}}"


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(prey) -> None:
        if not prey.hidden and isinstance(prey, Herbivore):
            prey.health -= 50
            if prey.health <= 0:
                Animal.alive.remove(prey)

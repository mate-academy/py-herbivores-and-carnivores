class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: "Herbivore") -> None:
        if (prey in Animal.alive and isinstance(prey, Herbivore)
                and prey.hidden is False):
            prey.health -= 50
            if prey.health <= 0:
                Animal.alive.remove(prey)

class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    bite_damage = 50

    def bite(self, prey: Herbivore) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health = prey.health - Carnivore.bite_damage
        if prey.health <= 0 and prey in Animal.alive:
            Animal.alive.remove(prey)

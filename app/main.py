class Animal:
    alive: list["Animal"] = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0 and self not in Animal.alive:
            Animal.alive.append(self)


    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Carnivore):
            return

        if prey.hidden:
            return

        prey.health -= 50
        prey.health = max(0, prey.health)

        if prey.health == 0 and prey in Animal.alive:
            Animal.alive.remove(prey)
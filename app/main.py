class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0:
            self.die()

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def die(self) -> None:
        if self in Animal.alive and self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(50)

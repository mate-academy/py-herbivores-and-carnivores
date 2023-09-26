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

    def update_health(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        Animal.alive.remove(self)
        self.health = 0

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, target: str) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.update_health(50)

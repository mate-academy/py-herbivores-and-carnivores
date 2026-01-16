class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def take_damage(self, damage: int) -> None:
        if self.health > 0:
            self.health -= damage
            print(
                f"{self.name} received {damage} damage! "
                f"Health {self.health} now."
            )
            if self.health <= 0:
                self.die()

    def die(self) -> None:
        print(f"{self.name} died.")
        Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.take_damage(50)

class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(herbivore: Herbivore) -> None:
        herbivores = [
            animal for animal in Animal.alive
            if isinstance(animal, Herbivore)
            and not animal.hidden
        ]
        if herbivores:
            target_herbivore = herbivores[0]
            target_herbivore.health -= 50
            if target_herbivore.health <= 0:
                target_herbivore.die()

class Animal:
    alive = []

    def __init__(
            self,
            name: str,
    ) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        if self not in Animal.alive:
            self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )

    def is_alive(self) -> int:
        return self.health > 0

    @staticmethod
    def remove_dead_animals() -> None:
        Animal.alive = [animal for animal in Animal.alive if animal.is_alive()]


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: str) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)

class AnimalList(list):
    def __str__(self) -> str:
        repr_instances = [repr(item) for item in self]
        return f"[{', '.join(repr_instances)}]"


class Animal:
    alive: AnimalList["Animal"] = AnimalList([])

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:
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
    def bite(
            self,
            animal: Animal
    ) -> None:
        if not isinstance(animal, Herbivore):
            return

        if animal.hidden:
            return

        animal.health -= 50
        if animal.health <= 0:
            animal.health = 0
            Animal.alive.remove(animal)

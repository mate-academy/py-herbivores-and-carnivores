class Animal:
    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        Animal.alive.append(self)

    def __repr__(self) -> str:
        return_string = f"{{Name: {self.name}, Health: {self.health}, "
        return_string += f"Hidden: {self.hidden}}}"
        return return_string

    alive = []


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, animal: Animal) -> None:
        if not isinstance(animal, Carnivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)

class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal_instance: Animal) -> None:
        if (
            isinstance(animal_instance, Herbivore)
            and not animal_instance.hidden
        ):
            animal_instance.health = animal_instance.health - 50
            if animal_instance.health <= 0:
                Animal.alive.remove(animal_instance)

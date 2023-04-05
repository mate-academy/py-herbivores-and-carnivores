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
        self.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        elif self.hidden is False:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, animal_name: Animal) -> None:
        if isinstance(animal_name, Herbivore) and animal_name.hidden is False:
            animal_name.health -= 50
            if animal_name.health <= 0:
                self.alive.remove(animal_name)

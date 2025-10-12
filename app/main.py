class Animal:

    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f""
                f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )

    def death(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> bool:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False
        return True


class Carnivore(Animal):

    @staticmethod
    def bite(animal: Animal) -> None:
        if animal.hidden is False and isinstance(animal, Herbivore):
            animal.health -= 50
        if animal.health <= 0:
            Animal.death(animal)

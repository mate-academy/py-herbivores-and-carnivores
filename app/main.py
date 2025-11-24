class Animal:
    alive: list["Animal"] = []

    def __init__(self,
                 name: str,
                 health: int = 100
                 ) -> None:
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def die(self) -> None:
        self.health = 0
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self,
             animal: Animal
             ) -> None:
        if animal in Animal.alive:
            if not animal.hidden and isinstance(animal, Herbivore):
                animal.health -= 50
                if animal.health <= 0:
                    animal.die()

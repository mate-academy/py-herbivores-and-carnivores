class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        if self.hidden:
            print(f"{self.name} is now hidden.")


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()
        elif isinstance(herbivore, Carnivore):
            print(f"{self.name} cannot bite another carnivore.")
        else:
            print(f"{self.name} cannot bite a hidden herbivore.")

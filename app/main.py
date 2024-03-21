class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def die(self) -> None:
        Animal.alive.remove(self)


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if isinstance(herbivore, Carnivore):
            return print("Carnivores cannot bite carnivor")
        if herbivore.hidden:
            return print("Cannot bite a hidden herbivore")

        herbivore.health -= 50
        if herbivore.health <= 0:
            print(f"{herbivore.name} is dead")
            herbivore.die()

class Animal:
    alive = []
    hidden = False

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = Animal.hidden
        Animal.alive.append(self)

    def die(self) -> None:
        self.health = 0
        if self in Animal.alive:
            Animal.alive.remove(self)
        print(f"{self.name} is died.")

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:
                prey.die()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

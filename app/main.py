class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def die(self) -> None:
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore):
            print(f"{self.name} can't bite another carnivore")
            return

        if isinstance(target, Herbivore):
            if target.hidden:
                print(f"{target.name} is hiding")
                return

            target.health -= 50
            if target.health <= 0:
                target.die()

        else:
            print("Target is not a herbivore")

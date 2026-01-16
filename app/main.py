class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
        status = "hidden" if self.hidden else "visible"
        print(f"{self.name} is now {status}.")


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if not isinstance(target, Herbivore):
            print(f"{self.name} cannot bite {target.name} (not a herbivore).")
            return

        if target.hidden:
            print(f"{self.name} cannot bite {target.name} (it is hidden).")
            return

        target.health -= 50
        if target.health <= 0:
            target.die()
            print(f"{target.name} has been eaten by {self.name}!")
        else:
            print(
                f"{self.name} bit {target.name}! Health left: {target.health}"
            )

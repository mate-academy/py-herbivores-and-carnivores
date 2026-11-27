class Animal:

    def __init__(
            self,
            name: str,
            health: int = 100
    ) -> None:

        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    alive: list["Animal"] = []

    def __repr__(
            self
    ) -> str:

        return (
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )


def check_alive(
        animal: Animal
) -> None:
    if animal in Animal.alive:
        if animal.health <= 0:
            Animal.alive.remove(animal)
            print(f"{animal.name} is dead")


class Herbivore(Animal):

    def hide(
            self
    ) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(
            self,
            target: Animal
    ) -> None:
        if isinstance(target, Herbivore):
            if not target.hidden:
                target.health -= 50
                check_alive(target)
            else:
                print(f"{self.name} cannot bite hidden {target.name}")

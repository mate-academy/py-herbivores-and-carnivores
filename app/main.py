class Animal:
    alive = []

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

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


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if herbivore.__class__ != Herbivore:
            print(f"{herbivore.name} is not a herbivore and cannot be bitten.")
        else:
            if herbivore.hidden:
                print(f"{herbivore.name} is hidden and cannot be bitten.")
            else:
                herbivore.health -= 50
                print(
                    f"{herbivore.name} is bitten and health is now "
                    f"{herbivore.health}."
                )
                if herbivore.health <= 0:
                    print(f"{herbivore.name} has died.")
                    Animal.alive.remove(herbivore)

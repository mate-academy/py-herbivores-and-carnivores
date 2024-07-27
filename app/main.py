class Animal:
    alive = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        self.__class__.alive.append(self)

    def take_damage(self, amount: int) -> None:
        self.health -= amount

    def make_dead(self) -> None:
        if self.health <= 0:
            print(f"{self.name} is dead")
            self.__class__.alive.remove(self)

    def __str__(self) -> str:
        return f"{self.name} (Health: {self.health})"

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name},"
            f" Health: {self.health},"
            f" Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    def bite(self, herbivore: "Herbivore") -> None:
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.take_damage(50)
            herbivore.make_dead()

        elif not isinstance(herbivore, Herbivore):
            print(f"{self.name} cannot bite another carnivore.")
        else:
            print(f"{herbivore.name} is hidden and cannot be bitten.")

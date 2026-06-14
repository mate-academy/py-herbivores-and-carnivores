class Animal:
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden

        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @staticmethod
    def remove_from_alive(animal: "Animal") -> None:
        if animal in Animal.alive:
            Animal.alive.remove(animal)

    def _check_health(self) -> None:
        if self.health <= 0:
            self.health = 0
            Animal.remove_from_alive(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if (
            isinstance(herbivore, Herbivore)
            and not herbivore.hidden
            and herbivore.health > 0
        ):
            herbivore.health -= 50
            herbivore._check_health()

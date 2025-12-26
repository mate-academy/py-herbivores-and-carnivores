class Animal:
    alive = list()

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}"
                               for key, value
                               in self.get_animal().items()) + "}"

    def __repr__(self) -> str:
        return str(self)

    def get_animal(self) -> dict:
        return dict(
            Name=self.name, Health=self.health, Hidden=self.hidden
        )

    def bite_animal(self) -> None:
        self.health -= 50
        if self.health <= 0:
            self.alive.remove(self)


class Carnivore(Animal):
    @staticmethod
    def bite(bitten_animal: Animal) -> None:
        if bitten_animal.hidden is not True and not isinstance(bitten_animal,
                                                               Carnivore):
            bitten_animal.bite_animal()


class Herbivore(Animal):
    def hide(self) -> None:
        if self.hidden is False:
            self.hidden = True
        else:
            self.hidden = False

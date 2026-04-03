class Animal:
    alive: list["Animal"] = []

    def __init__(
        self,
        name: str,
        health: int = 100
    ) -> None:
        self.name: str = name
        self.health: int = health
        self.hidden: bool = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(
        self,
        beast: Animal
    ) -> None:
        if isinstance(beast, Herbivore) and not beast.hidden:
            beast.health -= 50
            if beast.health <= 0 and beast in Animal.alive:
                Animal.alive.remove(beast)

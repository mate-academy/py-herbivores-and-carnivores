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
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(beast) -> None:
        if not isinstance(beast, Carnivore) and not beast.hidden:
            beast.health -= 50
        if beast.health <= 0:
            Animal.alive.remove(beast)

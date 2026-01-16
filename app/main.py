class Animal:
    alive = []

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

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def show_alive(cls) -> list:
        return [str(a) for a in cls.alive]

    def check_health(self) -> None:
        if isinstance(Animal.alive, list):
            if self.health <= 0 and self in Animal.alive:
                Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: "Herbivore") -> None:
        if isinstance(herbivore, Herbivore):
            if isinstance(herbivore, Herbivore) and not herbivore.hidden:
                herbivore.health -= 50
                herbivore.check_health()
